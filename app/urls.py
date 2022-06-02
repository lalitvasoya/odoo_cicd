from flask import Blueprint

from app.views import ApiTest

routes = Blueprint('routes', __name__)

routes.add_url_rule('/status', view_func=ApiTest.as_view('status'))
