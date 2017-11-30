from flask_classy import FlaskView
from flask import render_template


class TopView(FlaskView):
    route_base = '/'

    # /
    def index(self):
        return render_template("frontend/top/index.jade")

    # /dashboard
    def dashboard(self):
        return render_template("frontend/top/dashboard.jade")

    # /battle_history
    def battle_history(self):
        return render_template("frontend/top/battle_history.jade")

    # /setting
    def setting(self):
        return render_template("frontend/top/setting.jade")

    # /login
    def login(self):
        pass

    # /logout
    def logout(self):
        pass
