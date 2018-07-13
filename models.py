# models.py
from wsgi import db

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())


    def __repr__(self):
        return '<id {}>'.format(self.id)
    def __str__(self):
        return '%s - %s' % (self.id, self.name)
