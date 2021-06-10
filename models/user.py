import sqlite3
from db import db #importing the sqlalchemy

class UserModel(db.Model): 
    __tablename__ = 'users'  #telling the sqlalchemy about the tablename and its columns to make sure they are saved in the database.
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String)
    password=db.Column(db.String)


    def __init__(self,username, password):
        
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first() #This is the query builder which does select * from users where the column username = given username


        

    @classmethod
    def find_by_id(cls,_id):

        return cls.query.filter_by(id=_id).first()
        
