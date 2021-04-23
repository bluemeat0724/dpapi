from app.secure import *


class Config:
  SECRET_KEY = SECRET_KEY
  JSON_AS_ASCII = False
  JSON_SORT_KEYS = False
  UPLOAD_FOLDER = 'uploads/'
  ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

  @staticmethod
  def init_app(app):
    pass


class DevelopmentConfig(Config):
  DEBUG = True
  # SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
  SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI


class TestingConfig(Config):
  TESTING = True
  SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost:3306/report'


class ProductionConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:NetC@123@localhost:3306/report'


config = {'development': DevelopmentConfig,
          'testing': TestingConfig,
          'production': ProductionConfig,
          'default': DevelopmentConfig
          }
