import os

from flask import Flask
from flask_restful import Api #Resource and Api are two important factors where the Api would understand that it is using a particular resource. If api is student and then the resource is student
from flask_jwt import JWT
from resources.user import UserAdd

from security import authenticate, identity

from resources.item import Item,ItemsList

from resources.store import Store,StoresList



app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db') #To tell the SQLAlchemy where to look for 
if app.config['SQLALCHEMY_DATABASE_URI'].startswith("postgres://"):
    app.config['SQLALCHEMY_DATABASE_URI']= app.config['SQLALCHEMY_DATABASE_URI'].replace("postgres://", "postgresql://", 1)
app.secret_key="jose"
api=Api(app) 



jwt = JWT(app, authenticate, identity) #/auth

#items=[{"name":"chair",'price':50}]

# class Item(Resource):
    
#     parser=reqparse.RequestParser()
#     parser.add_argument('price', 
#             type=float,
#             required=True,
#             help="This field is mandatory"
#         )

#     @jwt_required()
#     def get(self,name):
#         for item in items:
#             if item['name']==name:
#                 return item
#     def post(self,name):
       

#         for i in items:
#             if i['name']==name:
#                 return {"message": "already exists"}
#             else:

#                 request_data=Item.parser.parse_args()
#                 item={
#                     "name":name,
#                     "price":request_data['price']
#                 }
#                 items.append(item)
#                 return {"items":items}

#     def delete(self,name):
#         for i in items:
#             if i['name']==name:
#                 items.remove(i)
#                 return {"message": "items deleted"}

#     def put(self,name):
#         parser=reqparse.RequestParser()
#         parser.add_argument('price',
#             type=float,
#             required=True,
#             help="This field is mandatory"
#         )

#         request_data = parser.parse_args() #We use the parser instead of the get_json() method because this way we could select which argument to be passed and the payload will have only them.
#         for i in items:
#             if i['name']!=name:
#                 item={
#                     "name":name,
#                     "price":request_data['price']
#                 }
#                 items.append(item)
#             else: #Because of the parser here the request data only only update the price not the name
#                 i.update(request_data) #This method could be used to update the values in dictionary
#                 return items
                

            
        


# class ItemsList(Resource):
#     def get(self):
#         return items



api.add_resource(Item,'/item/<string:name>') #The app.route is done like this where we are notifying that the api represents the item resource
api.add_resource(ItemsList,'/items')
api.add_resource(Store,'/store/<string:name>') #The app.route is done like this where we are notifying that the api represents the item resource
api.add_resource(StoresList,'/stores')
api.add_resource(UserAdd,'/register')

if __name__ =='__main__':
    from db import db
    db.init_app(app)
 
    app.run(port=5000) #optional