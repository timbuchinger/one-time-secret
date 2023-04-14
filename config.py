import os


BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False
    # DATABASE_ENCRYPTION_KEY = 'abcdefghijklmnopqrstuvwxyz123456'
    SECRET_KEY = os.getenv('SECRET_KEY', default='BAD_SECRET_KEY')
    if os.getenv('DATABASE_URL'):
        SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL').replace(
            "postgres://", "postgresql://", 1)
    else:
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASEDIR, 'app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    LOG_WITH_GUNICORN = os.getenv('LOG_WITH_GUNICORN', default=False)


class ProductionConfig(Config):
    FLASK_ENV = 'production'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI',
                                        default=f"sqlite:///{os.path.join(BASEDIR, 'test.db')}")
    WTF_CSRF_ENABLED = False
