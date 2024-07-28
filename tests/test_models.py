import unittest
from app import create_app, db
from app.models import Book

class BookModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_add_book(self):
        new_book = Book(bookname='Test Book', author='Test Author', num_of_pages=123)
        db.session.add(new_book)
        db.session.commit()
        book = Book.query.first()
        self.assertEqual(book.bookname, 'Test Book')
        self.assertEqual(book.author, 'Test Author')
        self.assertEqual(book.num_of_pages, 123)

if __name__ == '__main__':
    unittest.main()
