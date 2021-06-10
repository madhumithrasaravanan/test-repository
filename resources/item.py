#import sqlite3
from flask import Flask,request
from flask_restful import Resource,reqparse #Resource and Api are two important factors where the Api would understand that it is using a particular resource. If api is student and then the resource is student
from flask_jwt import JWT,jwt_required

from models.item import ItemModel

class Item(Resource):
    
    parser=reqparse.RequestParser()
    parser.add_argument('price',
            type=float,
            required=True,
            help="This field is mandatory"
        )
    
    parser.add_argument('store_id',
            type=int,
            required=True,
            help="This helps to retrieve store"
        )

    @jwt_required()
    def get(self,name):
        item=ItemModel.find_by_name(name)
        if item:
            return item.json()
        else:
            return {"message": "sorry cannot find the item"}

    def post(self,name):
        item=ItemModel.find_by_name(name)
        if item:
           return {"message":"The item already exists so cannot add the price"}
        else:

            request_data=Item.parser.parse_args()
            insert_item=ItemModel(name,request_data['price'],request_data['store_id'])
            insert_item.save_to_db()
            return {"message": insert_item.json()}

    def delete(self,name):
        item=ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"message": "the items are deleted"}
        else:
            return{"message": "cannot delete the item"}

        
        
    def put(self,name):
        # parser=reqparse.RequestParser()
        # parser.add_argument('price',
        #     type=float,
        #     required=True,
        #     help="This field is mandatory"
        # )

        #request_data = parser.parse_args() #We use the parser instead of the get_json() method because this way we could select which argument to be passed and the payload will have only them.
        
        request_data=Item.parser.parse_args()
        
        item=ItemModel.find_by_name(name)
        if item:
            item.price=request_data['price']
            item.save_to_db()
            return item.json()

        else:
            update_item=ItemModel(name,request_data['price'],request_data['store_id'])
            update_item.save_to_db()
            
            return update_item.json()
        
        
    
        
        
        
class ItemsList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]} #Here the ItemModel.query.all() extracts all the data available within the database. We have used the list comprehension here
       
        