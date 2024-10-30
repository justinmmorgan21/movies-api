from flask import Flask, request
import db

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route("/movies.json")
def index():
    return db.movies_all()

@app.route("/movies.json", methods=["POST"])
def create():
    name = request.form.get("name")
    year = request.form.get("year")
    genre = request.form.get("genre")
    return db.movies_create(name, year, genre)

@app.route("/movies/<id>.json")
def show(id):
    return db.movies_find_by_id(id)

@app.route("/movies/<id>.json", methods=["PATCH"])
def update(id):
    name = request.form.get("name")
    year = request.form.get("year")
    genre = request.form.get("genre")
    return db.movies_update_by_id(id, name, year, genre)