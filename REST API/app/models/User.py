from flask_restful import Resource, reqparse
from common.MySqlConfig import MySqlConfig
import simplejson as json


class User:
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

        conn = User.mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('spCreateUser', (_userName, _userEmail, _userPassword))
        data = cursor.fetchall()

        if len(data) is 0:
            conn.commit()
            cursor.close()
            conn.close()
            return {'StatusCode': '201', 'Message': 'User creation success'}
        else:
            return {'StatusCode': '1000', 'Message': str(data[0])}

    def getUser(self):
        conn = User.mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        return json.dumps(cursor.fetchall())
