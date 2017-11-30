from flask import jsonify, request
from flask_classy import FlaskView


class ApiView(FlaskView):
    route_base = '/api/'

    def index(self):
        return jsonify(
            {}
        )
