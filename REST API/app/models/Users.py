from flask_restful import Resource, reqparse
from common.MySqlConfig import MySqlConfig
from common.JsonParser import JsonParser


class Users:
    mysql = MySqlConfig.mysql

    # Parse the arguments
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

    def getAllUsers(self):
        conn = Users.mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT UserId, UserName, UserEmail FROM users;")
        results = JsonParser.parseToJson(cursor)
        cursor.close
        conn.close
        if not results:
            return {'StatusCode': '404', 'Message': '404 not found'}, 404
        return results

    def getUserDetails(self, userID):
        conn = Users.mysql.connect()
        cursor = conn.cursor()
        query = ("SELECT UserId, UserName, UserEmail FROM users WHERE UserId='%d'")
        cursor.execute(query % userID)
        results = JsonParser.parseToJson(cursor)
        cursor.close
        conn.close
        if not results:
            return {'StatusCode': '404', 'Message': '404 not found'}, 404
        return results

    def deleteUser(self, userID):
        conn = Users.mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spDeleteUser', str(userID))
        data = cursor.fetchall()
        if len(data) is 0:
            conn.commit()
            cursor.close()
            conn.close()
            return {'StatusCode': '201', 'Message': 'User deletion success'}
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
