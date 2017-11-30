from flask_classy import FlaskView
from flask import render_template, redirect, flash
from flask_login import logout_user, current_user, login_required


class SettingView(FlaskView):
    route_base = '/setting/'

    @login_required
    def index(self):
        return render_template("frontend/top/setting.jade")

    @login_required
    def update_iksm_session(self):
        # TODO: iksm_sessionの登録処理
        flash("iksm_sessionを登録しました")
        return redirect('/setting/')
