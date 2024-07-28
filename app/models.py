from app import db

class Bookstore(db.Model):
    __tablename__ = 'bookstore'
    bookname = db.Column(db.String(255), primary_key=True)
    author = db.Column(db.String(255), nullable=False)
    num_of_pages = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Bookstore {self.bookname}>'
