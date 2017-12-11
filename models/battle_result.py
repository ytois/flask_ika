from models import db
from models.battle_result_members import battle_result_members
from datetime import datetime, timedelta


class BattleResult(db.Model):
    __tablename__ = 'battle_results'

    id                          = db.Column(db.Integer, primary_key=True)
    battle_number               = db.Column(db.Integer, nullable=False) # ユーザー固有のバトルID
    user_id                     = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    stage_id                    = db.Column(db.Integer, db.ForeignKey('stages.id'), nullable=False)
    rule_id                     = db.Column(db.Integer, db.ForeignKey('rules.id'), nullable=False)
    game_mode_id                = db.Column(db.Integer, db.ForeignKey('game_modes.id'), nullable=False)
    player_battle_member_id     = db.Column(db.Integer, db.ForeignKey('battle_members.id'), nullable=False)

    start_time                  = db.Column(db.DateTime, nullable=False) # ゲーム開始時間
    created_at                  = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at                  = db.Column(db.DateTime, onupdate=datetime.utcnow)

    my_team_result_id           = db.Column(db.Integer, db.ForeignKey('team_results.id'), nullable=False)
    other_team_result_id        = db.Column(db.Integer, db.ForeignKey('team_results.id'), nullable=False)

    # ガチマのみ
    elapsed_time                = db.Column(db.Integer) # ゲーム時間(秒)
    estimate_gachi_power        = db.Column(db.Integer)
    my_team_count               = db.Column(db.Integer)
    other_team_count            = db.Column(db.Integer)

    # リグマのみ
    league_point                = db.Column(db.Float)
    max_league_point            = db.Column(db.Integer)
    my_estimate_league_point    = db.Column(db.Integer)
    other_estimate_league_point = db.Column(db.Integer)

    # ナワバリのみ
    win_meter                   = db.Column(db.Integer)
    my_team_percentage          = db.Column(db.Float)
    other_team_percentage       = db.Column(db.Float)

    # relation
    stage             = db.relationship('Stage', uselist=False, backref='battle_result', lazy=True)
    user              = db.relationship('User', uselist=False, backref='battle_result', lazy=True)
    rule              = db.relationship('Rule', uselist=False, backref='battle_result', lazy=True)
    game_mode         = db.relationship('GameMode', uselist=False, backref='battle_result', lazy=True)
    result            = db.relationship('TeamResult', uselist=False, lazy=True, foreign_keys="BattleResult.my_team_result_id")
    other_team_result = db.relationship('TeamResult', uselist=False, lazy=True, foreign_keys="BattleResult.other_team_result_id")
    player            = db.relationship('BattleMember', uselist=False, lazy=True)
    members           = db.relationship('BattleMember', uselist=True, lazy=True, secondary=battle_result_members)

    @property
    def end_time(self):
        if self.elapsed_time:
            return self.start_time + timedelta(seconds=self.elapsed_time)
        else:
            return None

    def to_dict(self, detail=False):
        response  = {}

        for key in ['battle_number', ]:
            value = self.__getattribute__(key)
            response[key] = value

        response['start_time'] = self.start_time.strftime('%F %H:%M:%S')
        response['stage'] = self.stage.name
        response['rule'] = self.rule.name
        response['result'] = self.my_team_result.name
        response['game_mode'] = self.game_mode.name
        response['player'] = self.player.to_dict()

        return response
