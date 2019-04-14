from flask import Flask
from flask_restful import Resource, Api, reqparse
from databaseManager.table import Table
from flask_cors import CORS
from flask import jsonify

app = Flask(__name__)
api = Api(app)
CORS(app)

category = reqparse.RequestParser()
task = reqparse.RequestParser()
task.add_argument('task', type=str)
category.add_argument('category', type=str)


class Categories(Resource):

    def get(self):

        return Table.get_categories(id), 200

    def post(self):
        args = category.parse_args()
        results = Table.post_category(args['category'])
        return results, 201



class Category(Resource):

    def put(self,id):
        args = category.parse_args()
        result = Table.update_category(id, args['category'])
        return result, 200

    def delete(self,id):
        result = Table.delete_category(id)
        return result, 204


class Tasks(Resource):

    def get(self, id):
        return Table.get_tasks(id), 200

    def post(self, id):
        args = task.parse_args()
        results = Table.post_task(id, args['task'])
        return results, 201


class Task(Resource):

    def get(self, id, tid):

        return Table.get_task(id, tid), 200

    def put(self, id, tid):
        args = task.parse_args()
        result = Table.update_task(id, tid, args['task'])
        return result, 200

    def delete(self, id, tid):
        result = Table.delete_task(id, tid)
        return result, 204


api.add_resource(Categories, '/categories')
api.add_resource(Category, '/categories/<id>')
api.add_resource(Tasks, '/categories/<id>/tasks')
api.add_resource(Task, '/categories/<id>/tasks/<tid>')

if __name__ == '__main__':
    app.run(debug=True)

