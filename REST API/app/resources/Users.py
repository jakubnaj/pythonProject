from flask_restful import Resource
from decorators.ErrorHandler import handle_error
from models.User import User



class Users(Resource):
    @handle_error
    def post(self):
        return User.creasteUser(self)
    @handle_error
    def get(self):
        return User.getUser(self)
