from models.user import UserModel
import sqlite3
from flask_restful import Resource,reqparse



class UserAdd(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username',
            type=str,
            required=True,
            help="This field is mandatory"
        )
    parser.add_argument('password',
            type=str,
            required=True,
            help="This field is mandatory"
        )
    def post(self):
        
        data=UserAdd.parser.parse_args()

        #We can do the below methodology by calling the find by username function which will check and retrieve before adding 
        #if User.find_by_username(data['username']): 
            #return {"message":"Cannot add and the already already exists" }
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        #I have also exxecuted this method to check if the user already exists and then added.
        select_query="SELECT username FROM users WHERE username=?"
        result=cursor.execute(select_query,(data['username'],))
        row=result.fetchone()
        if row is None:
            user=UserModel(data['username'],data['password'])
            user.save_to_db()
            return {"message": "users added"}
        else:
            return{"message":"already exists"}
        
        

        

        

    





