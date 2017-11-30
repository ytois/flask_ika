from models import db
from datetime import datetime
from flask.ext.login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    twitter_user_id = db.Column(db.Integer)
    screen_name = db.Column(db.String)
    access_token = db.Column(db.String)
    access_token_secret = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def create(self):
        db.session.add(self)
        db.session.commit()
