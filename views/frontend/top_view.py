from flask_classy import FlaskView
from flask import render_template, redirect, flash
from flask_login import logout_user, current_user, login_required


class TopView(FlaskView):
    route_base = '/'

    # /
    def index(self):
        flash('message')
        return render_template("frontend/top/index.jade")

    # /dashboard
    @login_required
    def dashboard(self):
        return render_template("frontend/top/dashboard.jade")

    # /battle_history
    @login_required
    def battle_history(self):
        return render_template("frontend/top/battle_history.jade")

    # /login
    def login(self):
        # ログイン自体はTwitterのみで行う
        if current_user.is_authenticated:
            flash('ログイン済みです')
            return redirect('/')
        else:
            return render_template("frontend/top/login.jade")

    # /logout
    def logout(self):
        if current_user.is_authenticated:
            logout_user()
            flash('ログアウトしました')

        return redirect('/')
