from models import db
from datetime import datetime
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    twitter_user_id = db.Column(db.Integer)
    screen_name = db.Column(db.String)
    access_token = db.Column(db.String)
    access_token_secret = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    switch_session = db.relationship('SwitchSession', uselist=False, backref='user', lazy=True)

    def add(self):
        db.session.add(self)
        return self

    def commit(self):
        return db.session.commit()

    @property
    def iksm_session(self):
        if self.switch_session:
            return self.switch_session.iksm_session
        else:
            return None
