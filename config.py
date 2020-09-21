import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'pbkdf2:sha256:150000$YMzIELwH$1a785c41d41a1c659ed2cd1568ef2571d11a6b95961d9edb91f7aa878a7b67b8'
    SQLALCHEMY_DATABASE_URI= "postgres://ykycvpylzpifmt:dfdd4e82a555336ad8133feedb971b0f25f3ba0653aaf69cab9298eddb250e1a@ec2-34-254-24-116.eu-west-1.compute.amazonaws.com:5432/d10bdpi7er82iu"
    DEBUG = False

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

    SSL_REDIDRECT = False





class ProductionConfig(Config):

    SSL_REDIRECT = True
