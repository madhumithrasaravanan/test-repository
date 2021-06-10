  
from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password): #This is to check if if the username nad password matches
    user = UserModel.find_by_username(username) #We are calling the function 
    if user and safe_str_cmp(user.password, password): #comparing if the usernames aand password is crct
        return user

def identity(payload): #JWT token function
    user_id = payload['identity'] #from the paylod we extract the userid
    return UserModel.find_by_id(user_id) #we then check if the userid exisyts