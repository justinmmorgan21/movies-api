import sqlite3

def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def initial_setup():
    conn = connect_to_db()
    conn.execute(
        """
        DROP TABLE IF EXISTS movies;
        """
    )
    conn.execute(
        """
        CREATE TABLE movies (
          id INTEGER PRIMARY KEY NOT NULL,
          name TEXT,
          year TEXT,
          genre TEXT
        );
        """
    )
    conn.commit()
    print("Table created successfully")

    movies_seed_data = [
        ("Billy Madison", "1996", "comedy"),
        ("Legally Blonde", "2021", "comedy"),
        ("Sweet Home Alabama", "2022", "comedy"),
    ]
    conn.executemany(
        """
        INSERT INTO movies (name, year, genre)
        VALUES (?,?,?)
        """,
        movies_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()


if __name__ == "__main__":
    initial_setup()

# INDEX
def movies_all():
    conn = connect_to_db()
    rows = conn.execute(
        """
        SELECT * FROM movies
        """
    ).fetchall()
    return [dict(row) for row in rows]

# CREATE
def movies_create(name, year, genre):
    conn = connect_to_db()
    row = conn.execute(
        """
        INSERT INTO movies (name, year, genre)
        VALUES (?, ?, ?)
        RETURNING *
        """,
        (name, year, genre),
    ).fetchone()
    conn.commit()
    return dict(row)

# SHOW 
def movies_find_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        SELECT * FROM movies
        WHERE id = ?
        """,
        (id,),
    ).fetchone()
    return dict(row)