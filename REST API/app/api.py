from flask import Flask, json
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask.ext.mysql import MySQL

app = Flask(__name__)
api = Api(app, prefix="/api/v1")

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin123'
app.config['MYSQL_DATABASE_DB'] = 'adwisedb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)


class CreateUser(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str, help='Email address to create user')
            parser.add_argument('password', type=str, help='Password to create user')
            args = parser.parse_args()

            _userEmail = args['email']
            _userPassword = args['password']

            conn = mysql.connect()
            cursor = conn.cursor()

            return {'Email': args['email'], 'Password': args['password']}

        except Exception as e:
            return {'error': str(e)}

    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            return json.dumps(cursor.fetchall())

        except Exception as e:
            return {'error': str(e)}


api.add_resource(CreateUser, '/CreateUser')
if __name__ == '__main__':
    app.run(debug=True)
