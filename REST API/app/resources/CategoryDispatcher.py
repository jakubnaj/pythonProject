from flask_restful import Resource
from decorators.ErrorHandler import handle_error
from models.Categories import Categories
from flask_httpauth import HTTPBasicAuth
from common.Authentication import Authentication

auth = HTTPBasicAuth()
adminAuth = HTTPBasicAuth()

Authentication.init(Authentication, auth, adminAuth)


class Category(Resource):
    @handle_error
    def get(self):
        return Categories.getAllCategories(self)

    @handle_error
    @adminAuth.login_required
    def post(self):
        return Categories.createCategory(self)


class singleCategory(Resource):
    @handle_error
    def get(self, categoryID):
        return Categories.getSingleCategory(self, categoryID)

    @handle_error
    @adminAuth.login_required
    def delete(self, categoryID):
        return Categories.deleteSingleCategory(self, categoryID)

    @handle_error
    @adminAuth.login_required
    def put(self, categoryID):
        return Categories.changeCategoryName(self, categoryID)
