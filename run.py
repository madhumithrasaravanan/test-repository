from app import app
from db import db

db.init_app(app)



@app.before_first_request #This will create the tables on their own 
def create_tables():
    db.create_all()