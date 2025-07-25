from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    genre = db.Column(db.String(50))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/book/suggest")
def suggest_book():
    books = Book.query.all()
    if books:
        book = random.choice(books)
        return jsonify({
            "title": book.title,
            "author": book.author,
            "genre": book.genre
        })
    return jsonify({"error": "No books found"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        if Book.query.count() == 0:
            sample_books = [
                Book(title="To Kill a Mockingbird", author="Harper Lee", genre="Fiction"),
                Book(title="1984", author="George Orwell", genre="Dystopian"),
                Book(title="Pride and Prejudice", author="Jane Austen", genre="Romance"),
                Book(title="The Hobbit", author="J.R.R. Tolkien", genre="Fantasy"),
                Book(title="The Great Gatsby", author="F. Scott Fitzgerald", genre="Classic")
            ]
            db.session.bulk_save_objects(sample_books)
            db.session.commit()
    app.run(debug=True)