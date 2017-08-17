from flask import Flask, Blueprint
from api.restplus import api
from api.endpoints.todos import ns as todos_namespace

app = Flask(__name__)

def initialize_app(flask_app):
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(todos_namespace)
    flask_app.register_blueprint(blueprint)

def main():
    initialize_app(app)
    app.run(debug=True)


if __name__ == '__main__':
    main()
