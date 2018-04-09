class BaseConfig(object):
    SECRET_KEY='makesure to set very secret key'
    INDEX_PER_PAGE = 9 
    ADMIN_PER_PAGE = 15

class DevelopmentConfig(BaseConfig):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+mysqldb://root:123456@localhost:3306/jobplus4_5?charset=utf8'

class ProductionConfig(BaseConfig):
    pass

class TestingConfig(BaseConfig):
    pass

configs={
        'development':DevelopmentConfig,
        'production':ProductionConfig,
        'testing':TestingConfig
        }
