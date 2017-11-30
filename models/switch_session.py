from models import db
from datetime import datetime


class SwitchSession(db.Model):
    __tablename__ = 'switch_sessions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    iksm_session = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def create(self):
        db.session.add(self)
        db.session.commit()
