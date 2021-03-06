from flask_restful import Resource
from decorators.ErrorHandler import handle_error
from models.Users import Users
from flask_httpauth import HTTPBasicAuth
from common.Authentication import Authentication

auth = HTTPBasicAuth()
adminAuth = HTTPBasicAuth()

Authentication.init(Authentication, auth, adminAuth)

class User(Resource):
    @handle_error
    @adminAuth.login_required
    def get(self):
        return Users.getAllUsers(self)

    @handle_error
    def post(self):
        return Users.createUser(self)


class SingleUser(Resource):
    @handle_error
    @auth.login_required
    def get(self, userID):
        return Users.getSingleUser(self, userID)

    @handle_error
    @adminAuth.login_required
    def delete(self, userID):
        return Users.deleteSingleUser(self, userID)


class ChangePassword(Resource):
    @handle_error
    @auth.login_required
    def put(self, userID):
        return Users.changePassword(self, userID)

class LoginUser(Resource):
    @handle_error
    @auth.login_required
    def get(self):
        return Users.loginUser(self);
