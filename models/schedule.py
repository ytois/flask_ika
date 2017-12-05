from models import db
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property


class Schedule(db.Model):
    __tablename__ = 'schedules'

    id           = db.Column(db.Integer, primary_key=True)
    stage_id     = db.Column(db.Integer, db.ForeignKey('stages.id'), nullable=False)
    rule_id      = db.Column(db.Integer, db.ForeignKey('rules.id'), nullable=False)
    game_mode_id = db.Column(db.Integer, db.ForeignKey('game_modes.id'), nullable=False)

    start_time   = db.Column(db.DateTime, nullable=False) # ゲーム開始時間
    end_time     = db.Column(db.DateTime, nullable=False) # ゲーム時間(秒)
    created_at   = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at   = db.Column(db.DateTime, onupdate=datetime.utcnow)

    # relation
    stage        = db.relationship('Stage', uselist=False, backref='schedules', lazy=True)
    rule         = db.relationship('Rule', uselist=False, backref='schedules', lazy=True)
    game_mode    = db.relationship('GameMode', uselist=False, backref='schedules', lazy=True)

    @hybrid_property
    def active(self):
        return datetime.now() <= self.end_time
