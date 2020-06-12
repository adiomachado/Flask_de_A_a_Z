import os, random, string

class Config(object):
    CSRF_ENABLE = True
    SECRET = '0c5604d33401437940499defe3bbe6c0dda45317a2ea62bfcbae6611f26f3e1f'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None

class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http://%s/%s' % (IP_HOST, PORT_HOST) #http://localhost:8000
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://adiomachado:Jds@230601!@localhost:3306/curso_flask'
   
app_config = {
    'development': DevelopmentConfig(),
    'testing': None,
    'production': None
}

app_active = os.getenv('FLASK_ENV')
if app_config is None:
    app_config = 'development'
