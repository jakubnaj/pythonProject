from flask_restful import Resource
from decorators.ErrorHandler import handle_error
from models.Advices import Advices
from flask_httpauth import HTTPBasicAuth
from common.Authentication import Authentication

auth = HTTPBasicAuth()
adminAuth = HTTPBasicAuth()

Authentication.init(Authentication, auth, adminAuth)


class Advice(Resource):
    @handle_error
    def get(self):
        return Advices.getAllAdvices(self)

    @handle_error
    @auth.login_required
    def post(self):
        return Advices.createAdvice(self)


class singleAdvice(Resource):
    @handle_error
    def get(self, adviceID):
        return Advices.getSingleAdvice(self, adviceID)

    @handle_error
    @adminAuth.login_required
    def delete(self, adviceID):
        return Advices.deleteSingleAdvice(self, adviceID)
