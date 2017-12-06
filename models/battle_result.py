from models import db
from datetime import datetime, timedelta

# 中間テーブル
battle_result_members = db.Table(
    'battle_result_members',
    db.metadata,
    db.Column('battle_result_id', db.Integer, db.ForeignKey('battle_results.id')),
    db.Column('battle_member_id', db.Integer, db.ForeignKey('battle_members.id'))
)


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
    elpased_time                = db.Column(db.Integer, nullable=False) # ゲーム時間(秒)
    created_at                  = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at                  = db.Column(db.DateTime, onupdate=datetime.utcnow)

    my_team_result_id           = db.Column(db.Integer, db.ForeignKey('team_results.id'), nullable=False)
    other_team_result_id        = db.Column(db.Integer, db.ForeignKey('team_results.id'), nullable=False)

    # ガチマのみ
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
    stage             = db.relationship('Stage', uselist=False, backref='result', lazy=True)
    user              = db.relationship('User', uselist=False, backref='result', lazy=True)
    rule              = db.relationship('Rule', uselist=False, backref='result', lazy=True)
    game_mode         = db.relationship('GameMode', uselist=False, backref='result', lazy=True)
    my_team_result    = db.relationship('TeamResult', uselist=False, backref='result', lazy=True)
    other_team_result = db.relationship('TeamResult', uselist=False, backref='result', lazy=True)
    player            = db.relationship('BattleMember', uselist=False, backref='result', lazy=True)
    members           = db.relationship('BattleMember', uselist=True, backref='result', lazy=True, secondary=battle_result_members)

    @property
    def end_time(self):
        return self.start_time + timedelta(seconds=self.elpased_time)
