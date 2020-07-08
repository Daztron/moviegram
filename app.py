from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.user import UserRegister, UserLogin, PasswordReset

from db import db

app = Flask(__name__)
app.secret_key = 'gkp'
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

jwt = JWTManager(app)

@app.before_first_request
def create_tables():
	db.create_all()

api.add_resource(UserRegister,'/moviegram/user')
api.add_resource(UserLogin,'/moviegram/user/login')
api.add_resource(PasswordReset,'/moviegram/user/reset_password')


if __name__ == '__main__':
	db.init_app(app)
	app.run(debug=True, port = 8666)