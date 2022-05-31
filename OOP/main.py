from flask import Flask, request
from flask_restful import Resource, Api
from User import User

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)

app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)


class Login(Resource):
    def post(self):
        user = User(
            request.form['email'],
            request.form['password']
        )
        if user.login() == 'true':
            access_token = create_access_token(identity=user.email)
            return access_token, 200
        else:
            return 'False', 200


class SignUp(Resource):
    def post(self):
        user = User(
            request.form['name'],
            request.form['email'],
            request.form['password']
        )
        user.save()
        access_token = create_access_token(identity=user.email)
        return access_token, 200


# JWT protected
class Books(Resource):
    @jwt_required()
    def get(self):
        return "Books!"


# Add routes
api.add_resource(Login, '/login/')
api.add_resource(SignUp, '/signup/')
api.add_resource(Books, '/books/')

if __name__ == '__main__':
    app.run(debug=True)
