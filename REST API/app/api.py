from flask import Flask
from flask_restful import Api
from resources.UserDispatcher import CreateUser, GetAllUsers, UserDetails
from common.MySqlConfig import MySqlConfig

app = Flask(__name__)
api = Api(app, prefix="/api/v1")
MySqlConfig.initDatabase(app)

api.add_resource(CreateUser, '/createUser')
api.add_resource(GetAllUsers, '/getAllUsers')
api.add_resource(UserDetails, '/userDetails/<int:userID>')
if __name__ == '__main__':
    app.run(debug=True)
