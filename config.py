class Config():
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:4798@localhost/pitches'


class DevConfig(Config):
    DEBUG = True
    
class ProdConfig(Config):
    pass


class TestConfig(Config):
    pass

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
    
}