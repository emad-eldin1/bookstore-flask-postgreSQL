from flask import Blueprint, request, jsonify
from app import db
from app.models import Book

bp = Blueprint('main', __name__)

@bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{
        'bookname': book.bookname,
        'author': book.author,
        'num_of_pages': book.num_of_pages
    } for book in books])

@bp.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(
        bookname=data['bookname'],
        author=data['author'],
        num_of_pages=data['num_of_pages']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added'}), 201
