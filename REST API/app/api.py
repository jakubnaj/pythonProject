from flask import Flask
from flask_restful import Api
from resources.UserDispatcher import CreateUser, GetAllUsers, User, ChangePassword
from resources.AdviceDispatcher import Advice, singleAdvice
from common.MySqlConfig import MySqlConfig


app = Flask(__name__)
api = Api(app, prefix="/api/v1")
MySqlConfig.initDatabase(app)


# User resources
api.add_resource(CreateUser, '/createUser')
api.add_resource(GetAllUsers, '/getAllUsers')
api.add_resource(ChangePassword, '/user/<int:userID>/changePassword')
api.add_resource(User, '/user/<int:userID>')

# Advice resources
api.add_resource(Advice, '/advice')
api.add_resource(singleAdvice, '/advice/<int:adviceID>')
if __name__ == '__main__':
    app.run(debug=True)
