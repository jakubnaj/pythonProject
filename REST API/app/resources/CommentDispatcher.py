from flask_restful import Resource
from decorators.ErrorHandler import handle_error
from models.Comments import Comments
from flask_httpauth import HTTPBasicAuth
from common.Authentication import Authentication

auth = HTTPBasicAuth()
adminAuth = HTTPBasicAuth()

Authentication.init(Authentication, auth, adminAuth)


class Comment(Resource):
    @handle_error
    @auth.login_required
    def post(self):
        return Comments.createComment(self)

    @handle_error
    @adminAuth.login_required
    def get(self):
        return Comments.getAllComments(self)


class singleComment(Resource):
    @handle_error
    @auth.login_required
    def get(self, commentID):
        return Comments.getSingleComment(self, commentID)

    @auth.login_required
    def put(self, commentID):
        return Comments.updateLikesQuantity(self, commentID)

    @adminAuth.login_required
    def delete(self, commentID):
        return Comments.deleteSingleComment(self, commentID)


class adviceComments(Resource):
    @handle_error
    def get(self, adviceID):
        return Comments.getAdviceComments(self, adviceID)
