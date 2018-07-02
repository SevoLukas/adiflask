from flask import Flask


def create_app():
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/
    """
    new_app = Flask(__name__)
    # app.register_blueprint(api)
    return new_app


app = create_app()
@app.route('/')
def hello_world():
    return 'Hello, World!'
