from flask_restplus import fields
from api.restplus import api

todo_model = api.model('Todo', {
    '_id': fields.Integer(readOnly=True, description='The unique identifier of a todo'),
    'description': fields.String(required=True, description='Todo description'),
    'done': fields.Boolean(required=True, description='Todo is done'),
    'createdAt': fields.DateTime
})
