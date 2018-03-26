from flask_restful import reqparse
from common.MySqlConfig import MySqlConfig
from datetime import datetime
from models.BaseModel import BaseModel


class Advices(BaseModel):
    mysql = MySqlConfig.mysql

    def getAllAdvices(self):
        return BaseModel.baseRequest(self, "SELECT * FROM advices;")

    def getSingleAdvice(self, adviceID):
        results = BaseModel.baseRequest(self, "SELECT * FROM advices WHERE Id='{0}'", adviceID)
        if not results:
            return {'message': 'Not found'}, 404
        return results

    def deleteSingleAdvice(self, adviceID):
        if not BaseModel.baseRequest(self, "SELECT * FROM advices WHERE Id='{0}'", adviceID):
            return {'StatusCode': '404', 'Message': '404 not found'}, 404
        BaseModel.baseRequest(self, "DELETE FROM advices WHERE Id='{0}'", adviceID)
        return {'message': 'Delete successful'}, 200

    def createAdvice(self):

        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, help='title', required=True)
        parser.add_argument('shortDescription', type=str, help='short description to be shown on main page',
                            required=True)
        parser.add_argument('categoryName', type=str, help='CategoryName', required=True)
        parser.add_argument('authorName', type=str, help='AuthorName', required=True)
        parser.add_argument('body', type=str, help='Content', required=True)
        args = parser.parse_args()

        _adviceTitle = args['title']
        _adviceShortDescription = args['shortDescription']
        _adviceCategoryName = args['categoryName']
        _adviceAuthorName = args['authorName']
        _adviceCreateDate = str(datetime.now())
        _adviceBody = args['body']

        conn = Advices.mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spCreateAdvice',
                        (_adviceTitle, _adviceShortDescription, _adviceCategoryName, _adviceAuthorName, _adviceCreateDate,
                         _adviceBody))
        data = cursor.fetchall()

        if len(data) is 0:
            conn.commit()
            cursor.close()
            conn.close()
            return {'message': 'Advice creation success'}
        else:
            return {'message': str(data[0])}
