from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, create_access_token

from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "username",
        type=str,
        required=True,
        help="This field cannot be blank!"
    )
    parser.add_argument(
        "password",
        type=str,
        required=True,
        help="This field cannot be blank!"
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        username = data.get("username")
        password = data.get("password")
        if username is None or password is None:
            return {"message": "username/password missing :| "}, 422
        if UserModel.find_by_uname(username=username):
            return {"message": "The username is taken. :( "} , 422
        user = UserModel(username=username)
        user.hash_password(password)
        user.add_to_db()
        return {"message": f"User {username} added successfully"}, 200

    @jwt_required
    def get(self):
        # current_user = get_jwt_identity() 
        usernames = []
        users = UserModel.get_usernames()
        for user in users:
            usernames.append(user.get_username())
        return usernames
    
    @jwt_required
    def delete(self):
        data = UserRegister.parser.parse_args()
        username = data.get("username")
        password = data.get("password")

        user = UserModel.find_by_uname(uname=uname)
        if user:
            user.delete_from_db()
        return {"message": "User no longer exists"}, 200

class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "username",
        type=str,
        required=True,
        help="This field cannot be blank!"
    )
    parser.add_argument(
        "password",
        type=str,
        required=True,
        help="This field cannot be blank!"
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        username = data.get("username")
        password = data.get("password")
        if username is None or password is None:
            return {"message": "username/password missing :| "}, 422
        user = UserModel.find_by_uname(username=username)
        if not user:
            return {"message": f"user {username} does not exist"}, 422
        if user.verify_password(password):
            access_token = create_access_token(identity=username)
            return {"message": "Login Successfull","access_token":access_token}, 200
        return {"message": "Password Incorrect"}, 400
    
class PasswordReset(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "username",
        type=str,
        required=True,
    )
    parser.add_argument(
        "current_password",
        type=str,
        required=True,
    )
    parser.add_argument(
        "new_password",
        type=str,
        required=True,
    )

    def post(self):
        data = PasswordReset.parser.parse_args()
        username = data.get("username")
        current_password = data.get("current_password")
        new_password = data.get("new_password")
        if username is None or current_password is None or new_password is None:
            return {"message": "username/passwords missing :| "}, 422
        user = UserModel.find_by_uname(username)
        if not user:
            return {"message":"Username incorrect :|"}, 422
        if user.verify_password(current_password):
            user.hash_password(new_password)
            user.add_to_db()
            return {"message":"Password changed successfully :)"}, 200
        return {"message":"Verification failed"}, 400