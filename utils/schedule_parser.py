from datetime import datetime
from models import db, Rule, GameMode, Schedule


# TODO: class名は仮
class StageSchedules:
    def __init__(self, _dict):
        self.__raw = _dict

    @property
    def league(self):
        return self.__fetch_stage('league')

    @property
    def gachi(self):
        return self.__fetch_stage('gachi')

    @property
    def regular(self):
        return self.__fetch_stage('regular')

    @property
    def all(self):
        schedules = []
        schedules.extend(self.league)
        schedules.extend(self.gachi)
        schedules.extend(self.regular)
        return schedules

    def save_db(self):
        """
        DBに保存する
        """
        schedules = []

        for stage in self.all:
            rule_id = Rule.find_by_key(stage.rule_key).id
            game_mode_id = GameMode.find_by_key(stage.game_mode_key).id

            for stage_id in stage.stage_ids:
                s = Schedule(
                    rule_id=rule_id,
                    game_mode_id=game_mode_id,
                    stage_id=stage_id,
                    start_time=stage.start_time,
                    end_time=stage.end_time
                )
                schedules.append(s)

        db.session.add_all(schedules)
        db.session.commit()

    def __fetch_stage(self, key):
        return [StageSchedule(stage) for stage in self.__raw[key]]


class StageSchedule:
    def __init__(self, _dict):
        self.__raw = _dict
        self.id = _dict['id']
        self.start_time = datetime.fromtimestamp(self.__raw['start_time'])
        self.end_time = datetime.fromtimestamp(self.__raw['end_time'])

    @property
    def rule_key(self):
        return self.__raw['rule']['key']

    @property
    def game_mode_key(self):
        return self.__raw['game_mode']['key']

    @property
    def stage_ids(self):
        # Apiの返すidは0から始まるのでDBには+1のIDで登録している
        stage_a = int(self.__raw['stage_a']['id']) + 1
        stage_b = int(self.__raw['stage_b']['id']) + 1
        return [stage_a, stage_b]
