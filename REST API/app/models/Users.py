from flask_restful import reqparse
from common.MySqlConfig import MySqlConfig
from models.BaseModel import BaseModel


class Users(BaseModel):
    mysql = MySqlConfig.mysql

    def getAllUsers(self):
        return BaseModel.baseRequest(self, "SELECT UserId, UserName, UserEmail FROM users;")

    def getSingleUser(self, userID):
        results = BaseModel.baseRequest(self, "SELECT * FROM users WHERE UserId='{0}'", userID)
        if not results:
            return {'StatusCode': '404', 'Message': '404 not found'}, 404
        return results

    def deleteSingleUser(self, userID):
        if not BaseModel.baseRequest(self, "SELECT * FROM users WHERE UserId='{0}'", userID):
            return {'StatusCode': '404', 'Message': '404 not found'}, 404
        BaseModel.baseRequest(self, "DELETE FROM users WHERE UserId='{0}'", userID)
        return {'StatusCode': '200', 'Message': 'Delete successful'}, 200

    def createUser(self):

        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, help='Nick', required=True)
        parser.add_argument('email', type=str, help='Email address to create user', required=True)
        parser.add_argument('password', type=str, help='Password to create user', required=True)
        args = parser.parse_args()

        _userName = args['name']
        _userEmail = args['email']
        _userPassword = args['password']

        conn = Users.mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spCreateUser', (_userName, _userEmail, _userPassword))
        data = cursor.fetchall()

        if len(data) is 0:
            conn.commit()
            cursor.close()
            conn.close()
            return {'StatusCode': '201', 'Message': 'User creation success'}, 201
        else:
            return {'StatusCode': '1000', 'Message': str(data[0])}

    def changePassword(self, userID):

        parser = reqparse.RequestParser()
        parser.add_argument('oldPassword', type=str, help='old Password', required=True)
        parser.add_argument('newPassword', type=str, help='new Password', required=True)
        args = parser.parse_args()

        _userId = userID
        _oldPassword = args['oldPassword']
        _newPassword = args['newPassword']

        conn = Users.mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spChangePassword', (_userId, _oldPassword, _newPassword))
        data = cursor.fetchall()

        if len(data) is 0:
            conn.commit()
            cursor.close()
            conn.close()
            return {'StatusCode': '200', 'Message': 'User password Changed'}
        else:
            return {'StatusCode': '1000', 'Message': str(data[0])}
