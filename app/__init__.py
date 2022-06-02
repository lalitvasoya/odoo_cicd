from flask import Flask


def create_app():
    app = Flask(__name__)

    with app.app_context():

        from app.urls import routes
        app.register_blueprint(routes)
        return app
