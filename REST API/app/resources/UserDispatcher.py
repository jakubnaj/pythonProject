from flask_restful import Resource
from decorators.ErrorHandler import handle_error
from models.Users import Users


class CreateUser(Resource):
    @handle_error
    def post(self):
        return Users.createUser(self)


class GetAllUsers(Resource):
    @handle_error
    def get(self):
        return Users.getAllUsers(self)


class User(Resource):
    @handle_error
    def get(self, userID):
        return Users.getUserDetails(self, userID)

    @handle_error
    def delete(self, userID):
        return Users.deleteUser(self, userID)


class ChangePassword(Resource):
    @handle_error
    def put(self, userID):
        return Users.changePassword(self, userID)
