import os

from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    @app.route('/index')
    def index():
        return render_template('index.html')
        
    
    return app