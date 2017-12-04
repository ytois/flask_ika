from models import db
from datetime import datetime


class TeamResult(db.Model):
    __tablename__ = 'team_results'

    id         = db.Column(db.Integer, primary_key=True)
    key        = db.Column(db.String, nullable=False)
    name       = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def add(self):
        db.session.add(self)
        return self

    def commit(self):
        return db.session.commit()
