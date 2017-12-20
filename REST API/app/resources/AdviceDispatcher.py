from flask_restful import Resource
from decorators.ErrorHandler import handle_error
from models.Advices import Advices


class Advice(Resource):
    @handle_error
    def get(self):
        return Advices.getAllAdvices(self)

    @handle_error
    def post(self):
        return Advices.createAdvice(self)


class singleAdvice(Resource):
    @handle_error
    def get(self, adviceID):
        return Advices.getSingleAdvice(self, adviceID)

    @handle_error
    def delete(self, adviceID):
        return Advices.deleteSingleAdvice(self, adviceID)
