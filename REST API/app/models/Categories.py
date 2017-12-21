from flask_restful import Resource, reqparse
from common.MySqlConfig import MySqlConfig
from common.JsonParser import JsonParser
from models.BaseModel import BaseModel


class Categories(BaseModel):
    mysql = MySqlConfig.mysql

    def getAllCategories(self):
        return BaseModel.baseRequest(self, "SELECT * FROM categories;")

    def createCategory(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, help='Category Name', required=True)
        args = parser.parse_args()

        _name = args['name']
        if Categories.IsCategoryNameExists(self, _name):
            return {'error': 'Category name already exists'}, 200

        BaseModel.baseRequest(self, "Insert Into categories(Name) values ('{0}') ", _name)
        return {'StatusCode': '201', 'Message': 'Category creation success'}, 201

    def getSingleCategory(self, categoryID):
        results = BaseModel.baseRequest(self, "SELECT * FROM categories WHERE Id='{0}'", categoryID)
        if not results:
            return {'StatusCode': '404', 'Message': '404 not found'}, 404
        return results

    def deleteSingleCategory(self, categoryID):
        if not BaseModel.baseRequest(self, "SELECT * FROM categories WHERE Id='{0}'", categoryID):
            return {'StatusCode': '404', 'Message': '404 not found'}, 404
        BaseModel.baseRequest(self, "DELETE FROM categories WHERE Id='{0}'", categoryID)
        return {'StatusCode': '200', 'Message': 'Delete successful'}, 200

    def IsCategoryNameExists(self, name):
        if not BaseModel.baseRequest(self, "SELECT * FROM categories WHERE name='{0}'", name):
            return False
        return True

    def changeCategoryName(self, categoryID):
        parser = reqparse.RequestParser()
        parser.add_argument('newName', type=str, help='old Password', required=True)
        args = parser.parse_args()

        _categoryID = categoryID
        _newName = args['newName']
        if not BaseModel.baseRequest(self, "SELECT * FROM categories WHERE Id='{0}'", categoryID):
            return {'StatusCode': '404', 'Message': '404 not found'}, 404
        if Categories.IsCategoryNameExists(self, _newName):
            return {'error': 'Category name already exists'}, 200

        BaseModel.baseRequest(self, "UPDATE categories SET name = '{0}' WHERE id='{1}'", _newName, _categoryID)
        return {'StatusCode': '200', 'Message': 'Category Updated'}
