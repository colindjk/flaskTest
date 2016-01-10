# default config
import os
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\xe4\xf1\x821X\xc8\x03\xec\xf9\xbc\xb6h\xc4\x90\xb8=?\x95>\x04d\xcap\x1c'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    print SQLALCHEMY_DATABASE_URI

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False # this must be false, else security issue ensues. 
