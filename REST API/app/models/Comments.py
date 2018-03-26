from flask_restful import reqparse
from common.MySqlConfig import MySqlConfig
from datetime import datetime
from models.BaseModel import BaseModel


class Comments(BaseModel):
    mysql = MySqlConfig.mysql

    def getAllComments(self):
        return BaseModel.baseRequest(self, "SELECT * FROM comments;")

    def getSingleComment(self, commentID):
        results = BaseModel.baseRequest(self, "SELECT * FROM comments WHERE ID='{0}'", commentID)
        if not results:
            return {'message': 'Not found'}, 404
        return results

    def getAdviceComments(self, adviceID):
        results = BaseModel.baseRequest(self, "SELECT * FROM comments WHERE adviceID='{0}'", adviceID)
        BaseModel.baseRequest(self, "UPDATE advices SET ViewsQuantity = ViewsQuantity + 1 WHERE Id='{0}'", adviceID)
        return results

    def deleteSingleComment(self, commentID):
        if not BaseModel.baseRequest(self, "SELECT * FROM comments WHERE Id='{0}'", commentID):
            return {'message': 'Not found'}, 404
        BaseModel.baseRequest(self, "DELETE FROM comments WHERE Id='{0}'", commentID)
        return {'message': 'Delete successful'}, 200

    def createComment(self):
        parser = reqparse.RequestParser()
        parser.add_argument('adviceID', type=int, help='AdviceID', required=True)
        parser.add_argument('authorName', type=str, help='AuthorName',
                            required=True)
        parser.add_argument('content', type=str, help='Comment body', required=True)
        parser.add_argument('likesQuantity', type=int, help='Number of Likes', required=True)
        args = parser.parse_args()

        _adviceID = args['adviceID']
        _authorName = args['authorName']
        _createDate = str(datetime.now())
        _content = args['content']
        _likesQuantity = args['likesQuantity']

        conn = Comments.mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spCreateComment',
                        (_adviceID, _authorName, _createDate, _content, _likesQuantity))
        data = cursor.fetchall()

        if len(data) is 0:
            conn.commit()
            cursor.close()
            conn.close()
            BaseModel.baseRequest(self, "UPDATE advices SET CommentsQuantity = CommentsQuantity + 1 WHERE Id='{0}'", _adviceID)
            return {'message': 'Comment creation success'}, 201
        else:
            return {'message': str(data[0])}
