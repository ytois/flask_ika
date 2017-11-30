from models import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    access_token = db.Column(db.String)
    access_token_secret = db.Column(db.String)
