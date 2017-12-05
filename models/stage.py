from models import db
from datetime import datetime


class Stage(db.Model):
    __tablename__ = 'stages'

    id = db.Column(db.Integer, primary_key=True)
    stage_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def add(self):
        db.session.add(self)
        return self

    def commit(self):
        return db.session.commit()

    @classmethod
    def save_from_dict(self, _dict):
        if Stage.query.filter_by(stage_id=int(_dict['id'])).first():
            return None

        stage = Stage(
            id=(1 + int(_dict['id'])),
            stage_id=int(_dict['id']),
            name=_dict['name'],
            image=_dict['image'],
        )

        return stage.add().commit()

    def to_dict(self):
        return {
            'id': self.stage_id,
            'image': self.image,
            'name': self.name
        }
