from flask_restful import Resource, reqparse
from common.MySqlConfig import MySqlConfig
from common.JsonParser import JsonParser
from flask_httpauth import HTTPBasicAuth

class Authentication:
    mysql = MySqlConfig.mysql

    def getUserPassword(self, username):
        conn = Authentication.mysql.connect()
        cursor = conn.cursor()
        query = ("SELECT UserPassword FROM users WHERE UserName ='%s';")
        cursor.execute(query % username)
        results = JsonParser.parseToJson(cursor)
        cursor.close
        conn.close
        if not results:
            return False
        return results[0].get("UserPassword")

    def init(self, auth, adminAuth):

        @auth.verify_password
        def verify(username, password):
            if not (username and password):
                return False
            userPassword = Authentication.getUserPassword(Authentication, username)
            return userPassword == password

        @adminAuth.verify_password
        def verify(username, password):
            if not (username and password):
                return False
            userPassword = Authentication.getUserPassword(Authentication, username)
            return username == "admin" and userPassword == password
