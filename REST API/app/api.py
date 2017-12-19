from flask import Flask
from flask_restful import Api
from resources.Users import Users
from common.MySqlConfig import MySqlConfig

app = Flask(__name__)
api = Api(app, prefix="/api/v1")
MySqlConfig.initDatabase(app)

api.add_resource(Users, '/users')
if __name__ == '__main__':
    app.run(debug=True)
