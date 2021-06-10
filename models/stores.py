#from models.item import ItemModel
from db import db


class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    items=db.relationship('ItemModel',lazy='dynamic') #Here the items variable will include a list of items which belongs to the same store id
  

    def __init__(self, name):
        self.name = name
        
    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]} #Here the self.items.all() will act as the qery builder which extracts all the data from the items table

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
