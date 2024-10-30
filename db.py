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