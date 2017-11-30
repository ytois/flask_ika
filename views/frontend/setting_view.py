from flask_classy import FlaskView, route
from flask import render_template, redirect, flash, request
from flask_login import current_user, login_required
from models import SwitchSession


class SettingView(FlaskView):
    route_base = '/setting/'

    @login_required
    def index(self):
        return render_template("frontend/top/setting.jade")

    @login_required
    @route('/update/', methods=['POST'])
    def update(self):
        switch_session = current_user.switch_session or SwitchSession(user_id=current_user.id)
        switch_session.iksm_session = request.form['iksm_session']
        switch_session.add().commit()

        flash("iksm_sessionを登録しました")
        return redirect('/setting/')
