import os

from flask import Flask

def create_app():
    app = Flask(__name__)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return "Hello, welcome!"
    
    return app