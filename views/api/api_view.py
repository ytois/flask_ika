from flask import jsonify
from flask_classy import FlaskView


class ApiView(FlaskView):

    def index(self):
        return jsonify(
            {}
        )
