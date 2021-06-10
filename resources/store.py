from models.stores import StoreModel
from flask import Flask,request
from flask_restful import Resource,reqparse #Resource and Api are two important factors where the Api would understand that it is using a particular resource. If api is student and then the resource is student
from flask_jwt import JWT,jwt_required

from models.stores import StoreModel

class Store(Resource):
    
   
    def get(self,name):
        store=StoreModel.find_by_name(name)
        if store:
            return store.json()
        else:
            return {"message": "sorry cannot find the store"}

    def post(self,name):
        store=StoreModel.find_by_name(name)
        if store:
           return {"message":"The store already exists so cannot add the store"}
        else:

            
            insert_item=StoreModel(name)
            insert_item.save_to_db()
            return{"store": insert_item.json()}
         


    def delete(self,name):
        store=StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {"message": "the store is deleted"}
        else:
            return{"message": "cannot delete the store"}


class StoresList(Resource):
    def get(self):
        return {'stores': [item.json() for item in StoreModel.query.all()]}