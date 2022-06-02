from flask import Blueprint

from app.views import ApiTest, Factorial

routes = Blueprint('routes', __name__)

routes.add_url_rule('/status', view_func=ApiTest.as_view('status'))
routes.add_url_rule('/fact', view_func=Factorial.as_view('fact'))
