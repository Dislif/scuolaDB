import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    '''user = 'root'
    password = ' '
    host = '127.0.0.1'
    port = 3306
    database = 'scuoladb'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql:///{}:{}@{}:{}/{}'.format(user, password, host, port, database)
    
    '''
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'scuola.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False