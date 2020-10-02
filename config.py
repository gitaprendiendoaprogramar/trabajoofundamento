import os

class Config(objecto):
    SECRET_KEY = "my_secret_key"

 class DevelopmentConfig(Config):
     DEBUG = True
     SQLALCHEMY_DATABASE_URI = "mysql://root:@localhost/flask" 