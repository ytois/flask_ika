from flask import jsonify, request
from flask_classy import FlaskView, route
from flask_login import login_required
from models import Schedule


class ApiView(FlaskView):
    route_base = '/api/'
    decorators = [login_required]

    @route('/user/setting/', methods=['POST'])
    def user_setting(self):
        pass

    def schedules(self):
        schedules = Schedule.query.filter(Schedule.active).order_by(Schedule.start_time)
        response = {'regular': {}, 'gachi': {}, 'league': {}}

        for schedule in schedules:
            game_mode = schedule.game_mode.name_en
            start_time = str(schedule.start_time)

            # 直近3つまで
            if len(response[game_mode]) >= 3 and start_time not in response[game_mode]:
                continue

            # キーが無ければ代入
            if start_time in response[game_mode]:
                response[game_mode][start_time].append(schedule.stage.to_dict())
            else:
                response[game_mode][start_time] = [schedule.stage.to_dict()]

        return jsonify(response)
