from flask_restplus import Resource
from api.restplus import api
from api.serializers import todo_model

ns = api.namespace('todos', description='Operations related to todos')

@ns.route('/')
class TodoCollection(Resource):
    def get(self):
        """
        Returns list of todos.
        """
        return "Ok"

    @api.expect(todo_model)
    def post(self):
        """
        Creates a new todo.
        """
        return "Ok", 201

@ns.route('/<int:id>')
class TodoItem(Resource):

    @api.marshal_with(todo_model)
    def get(self, id):
        """
        Returns a todo.
        """
        return "Ok"

    @api.expect(todo_model)
    def put(self, id):
        """
        Updates a todo.
        """
        return "Ok"

    @api.response(204, 'Todo successfully deleted.')
    def delete(self, id):
        """
        Deletes a todo.
        """
        return "Ok", 204
