from flask.views import MethodView
from flask import jsonify, request


class ApiTest(MethodView):

    def get(self):
        return jsonify({"status": "Flask testing!"})


class Factorial(MethodView):

    def _fact(self, n):
        if n == 0:
            return 1
        return n * self._fact(n - 1)

    def get(self):
        no = int(request.args.get('no', 1))
        return jsonify({"fact": self._fact(no)})
