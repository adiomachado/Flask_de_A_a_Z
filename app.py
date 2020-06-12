from flask import Flask
from flask_sqlalchemy import SQLALchemy
from config import app_config, app_active

config = app_config[app_active]

def create_app(config_name):
    app = Flask(__name__, template_folder='templates')

    app.secret_key = config.SECRET
    app.config.from_object(app_config[app_active])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   # retira a mensagem do flask
    db = SQLALchemy(app)             #cria a instancia do objeto em execucao (Flask)
    db.init_app(app)

    @app.route('/')
    def index():
        return 'Hello World!'

    return app