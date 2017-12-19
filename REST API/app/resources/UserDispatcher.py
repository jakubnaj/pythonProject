from flask_restful import Resource
from decorators.ErrorHandler import handle_error
from models.User import User


class CreateUser(Resource):
    # @handle_error
    # def get(self, userID):
    #     return User.getUser(self, userID)

    @handle_error
    def post(self):
        return User.createUser(self)


class GetAllUsers(Resource):
    @handle_error
    def get(self):
        return User.getAllUsers(self)

class UserDetails(Resource):
    @handle_error
    def get(self, userID):
        return User.getUserDetails(self, userID)

