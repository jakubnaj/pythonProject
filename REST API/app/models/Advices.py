from flask_restful import reqparse
from common.MySqlConfig import MySqlConfig
from common.JsonParser import JsonParser
from datetime import datetime
from models.BaseModel import BaseModel


class Advices(BaseModel):
    mysql = MySqlConfig.mysql

    def getAllAdvices(self):
        return BaseModel.baseRequest(self, "SELECT * FROM advices;")

    def getSingleAdvice(self, adviceID):
        results = BaseModel.baseRequest(self, "SELECT * FROM advices WHERE Id='{0}'", adviceID)
        if not results:
            return {'StatusCode': '404', 'Message': '404 not found'}, 404
        return results

    def deleteSingleAdvice(self, adviceID):
        if not BaseModel.baseRequest(self, "SELECT * FROM advices WHERE Id='{0}'", adviceID):
            return {'StatusCode': '404', 'Message': '404 not found'}, 404
        BaseModel.baseRequest(self, "DELETE FROM advices WHERE Id='{0}'", adviceID)
        return {'StatusCode': '200', 'Message': 'Delete successful'}, 200

    def createAdvice(self):

        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, help='title', required=True)
        parser.add_argument('shortDescription', type=str, help='short description to be shown on main page',
                            required=True)
        parser.add_argument('categoryID', type=int, help='CategoryID', required=True)
        parser.add_argument('authorID', type=int, help='AuthorID', required=True)
        parser.add_argument('body', type=str, help='Content', required=True)
        args = parser.parse_args()

        _adviceTitle = args['title']
        _adviceShortDescription = args['shortDescription']
        _adviceCategoryID = args['categoryID']
        _adviceAuthorID = args['authorID']
        _adviceCreateDate = str(datetime.now())
        _adviceBody = args['body']

        conn = Advices.mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spCreateAdvice',
                        (_adviceTitle, _adviceShortDescription, _adviceCategoryID, _adviceAuthorID, _adviceCreateDate,
                         _adviceBody))
        data = cursor.fetchall()

        if len(data) is 0:
            conn.commit()
            cursor.close()
            conn.close()
            return {'StatusCode': '201', 'Message': 'Advice creation success'}
        else:
            return {'StatusCode': '1000', 'Message': str(data[0])}
