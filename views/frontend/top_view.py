from flask_classy import FlaskView
from flask import render_template


class TopView(FlaskView):
    # /top/
    def index(self):
        return render_template("frontend/top.jade")

    # /top/information/
    def information(self):
        return 'infomation page'
