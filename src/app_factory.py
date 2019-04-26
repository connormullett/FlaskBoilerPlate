
from flask import Flask, jsonify

from .config import app_config
from .models import db, bcrypt

from .views.example_views import example_api


def create_app(env_name):
    '''
    Creates the Flask app object
    further configuration can be added
    here such as Flask-Cors and Flask-Heroku
    for Heroku deployment
    '''

    if not env_name:
        env_name = 'development'

    app = Flask(__name__)

    app.config.from_object(app_config[env_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # blueprint located in src/views/example_views.py
    app.register_blueprint(example_api, url_prefix='/api')

    @app.route('/')
    def endpoint():
        return jsonify({
            'status': 'success',
            'message': 'navigate to localhost:5000/api/ for another example' \
                    'send a POST request to that endpoint if you\' feeling brave'
        })

    bcrypt.init_app(app)
    db.init_app(app)

    return app

