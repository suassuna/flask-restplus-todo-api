from flask_restplus import Resource
from api.restplus import api

ns = api.namespace('todos', description='Operations related to todos')

@ns.route('/')
class TodoCollection(Resource):
    def get(self):
        """
        Returns list of todos.
        """
        return "Ok"

    def post(self):
        """
        Creates a new todo.
        """
        return "Ok"
