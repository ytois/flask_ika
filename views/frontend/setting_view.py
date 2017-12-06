from flask_classy import FlaskView, route
from flask import render_template, redirect, flash, request
from flask_login import current_user, login_required
from models import db, SwitchSession


class SettingView(FlaskView):
    route_base = '/setting/'

    @login_required
    def index(self):
        return render_template("frontend/top/setting.jade")

    @login_required
    @route('/update/', methods=['POST'])
    def update(self):
        current_user.screen_name = request.form['screen_name']
        iksm_session = request.form['iksm_session']

        if current_user.switch_session:
            current_user.switch_session.iksm_session = iksm_session
        else:
            current_user.switch_session = SwitchSession(iksm_session=iksm_session)

        db.session.add(current_user)
        db.session.commit()

        flash("情報を更新しました")
        return redirect('/setting/')
