from flask_restful import Resource, reqparse
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

    def get(self):
        usernames = []
        users = UserModel.get_usernames()
        for user in users:
            usernames.append(user.get_username())
        return usernames
    
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
            return {"message": "Login Successfull"}, 200
        return {"message": "Password Incorrect"}, 400