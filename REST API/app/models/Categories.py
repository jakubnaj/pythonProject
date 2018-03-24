from flask_restful import Resource, reqparse
from models.BaseModel import BaseModel


class Categories(BaseModel):
    def getAllCategories(self):
        return BaseModel.baseRequest(self, "SELECT * FROM categories;")

    def getSingleCategory(self, categoryID):
        results = BaseModel.baseRequest(self, "SELECT * FROM categories WHERE Id='{0}'", categoryID)
        if not results:
            return {'message': 'Not found'}, 404
        return results

    def deleteSingleCategory(self, categoryID):
        if not BaseModel.baseRequest(self, "SELECT * FROM categories WHERE Id='{0}'", categoryID):
            return {'message': 'Not found'}, 404
        BaseModel.baseRequest(self, "DELETE FROM categories WHERE Id='{0}'", categoryID)
        return {'message': 'Delete successful'}, 200

    def changeCategoryName(self, categoryID):
        parser = reqparse.RequestParser()
        parser.add_argument('newName', type=str, help='old Password', required=True)
        args = parser.parse_args()

        _categoryID = categoryID
        _newName = args['newName']
        if not BaseModel.baseRequest(self, "SELECT * FROM categories WHERE Id='{0}'", categoryID):
            return {'message': 'Not found'}, 404
        if Categories.IsCategoryNameExists(self, _newName):
            return {'message': 'Category name already exists'}, 200

        BaseModel.baseRequest(self, "UPDATE categories SET name = '{0}' WHERE id='{1}'", _newName, _categoryID)
        return {'message': 'Category Updated'}

    def createCategory(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, help='Category Name', required=True)
        args = parser.parse_args()

        _name = args['name']
        if Categories.IsCategoryNameExists(self, _name):
            return {'message': 'Category name already exists'}, 200

        BaseModel.baseRequest(self, "Insert Into categories(Name) values ('{0}') ", _name)
        return {'message': 'Category creation success'}, 201

    def IsCategoryNameExists(self, name):
        if not BaseModel.baseRequest(self, "SELECT * FROM categories WHERE name='{0}'", name):
            return False
        return True
