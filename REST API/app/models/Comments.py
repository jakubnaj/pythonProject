from flask_restful import reqparse
from common.MySqlConfig import MySqlConfig
from common.JsonParser import JsonParser
from datetime import datetime


class Comments:
    mysql = MySqlConfig.mysql

    def createComment(self):
        parser = reqparse.RequestParser()
        parser.add_argument('adviceID', type=int, help='AdviceID', required=True)
        parser.add_argument('authorID', type=int, help='AuthorID',
                            required=True)
        parser.add_argument('content', type=str, help='Comment body', required=True)
        parser.add_argument('likesQuantity', type=int, help='Number of Likes', required=True)
        args = parser.parse_args()

        _adviceID = args['adviceID']
        _authorID = args['authorID']
        _content = args['content']
        _createDate = str(datetime.now())
        _likesQuantity = args['likesQuantity']

        conn = Comments.mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spCreateComment',
                        (_adviceID, _authorID, _content, _createDate, _likesQuantity))
        data = cursor.fetchall()

        if len(data) is 0:
            conn.commit()
            cursor.close()
            conn.close()
            return {'StatusCode': '201', 'Message': 'Comment creation success'}, 201
        else:
            return {'StatusCode': '1000', 'Message': str(data[0])}

    def getAllComments(self):
        conn = Comments.mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM comments;")
        results = JsonParser.parseToJson(cursor)
        cursor.close
        conn.close
        return results

    def getSingleComment(self, commentID):
        conn = Comments.mysql.connect()
        cursor = conn.cursor()
        query = ("SELECT * FROM comments WHERE ID='%d'")
        cursor.execute(query % commentID)
        results = JsonParser.parseToJson(cursor)
        cursor.close
        conn.close
        if not results:
            return {'StatusCode': '404', 'Message': '404 not found'}, 404
        return results

    def deleteSingleComment(self, commentID):
        conn = Comments.mysql.connect()
        cursor = conn.cursor()
        query = ("DELETE FROM comments WHERE ID='%d'")
        cursor.execute(query % commentID)
        data = cursor.fetchall()
        if len(data) is 0:
            conn.commit()
            cursor.close()
            conn.close()
            return {'StatusCode': '200', 'Message': 'Comment deletion success'}
        else:
            return {'StatusCode': '1000', 'Message': str(data[0])}

    def getAdviceComments(self, adviceID):
        conn = Comments.mysql.connect()
        cursor = conn.cursor()
        query = ("SELECT * FROM comments WHERE adviceID ='%d';")
        cursor.execute(query % adviceID)
        results = JsonParser.parseToJson(cursor)
        cursor.close
        conn.close
        return results
