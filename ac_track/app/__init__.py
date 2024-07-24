from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

db = SQLAlchemy()
jwt = JWTManager()





migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()

    return app

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object('config.Config')
#
#     db.init_app(app)
#     jwt.init_app(app)
#
#     with app.app_context():
#         from . import routes
#         db.create_all()
#
#     return app
