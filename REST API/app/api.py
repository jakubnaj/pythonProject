from flask import Flask
from flask_restful import Api
from resources.UserDispatcher import User, ChangePassword, SingleUser
from resources.AdviceDispatcher import Advice, singleAdvice
from resources.CommentDispatcher import Comment, singleComment, adviceComments
from resources.CategoryDispatcher import Category, singleCategory
from common.MySqlConfig import MySqlConfig

app = Flask(__name__)
api = Api(app, prefix="/api/v1")
MySqlConfig.initDatabase(app)

# Users resources
api.add_resource(User, '/user')
api.add_resource(ChangePassword, '/user/<int:userID>/changePassword')
api.add_resource(SingleUser, '/user/<int:userID>')

# Advices resources
api.add_resource(Advice, '/advice')
api.add_resource(singleAdvice, '/advice/<int:adviceID>')

# Comments resources
api.add_resource(Comment, '/comment')
api.add_resource(singleComment, '/comment/<int:commentID>')
api.add_resource(adviceComments, '/adviceComments/<int:adviceID>')

# Categories resources
api.add_resource(Category, '/category')
api.add_resource(singleCategory, '/category/<int:categoryID>')
if __name__ == '__main__':
    app.run(debug=True)
