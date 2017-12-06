from models import db
from datetime import datetime


class BattleMember(db.Model):
    __tablename__ = 'battle_members'

    id                          = db.Column(db.Integer, primary_key=True)
    battle_number               = db.Column(db.Integer, nullable=False) # ユーザー固有のバトルID
    created_at                  = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at                  = db.Column(db.DateTime, onupdate=datetime.utcnow)

    principal_id                   = db.Column(db.String, nullable=False) # principal_id
    udemae                      = db.Column(db.JSON)
    # udemae ex. {'is_number_reached': False, 'name': 'S+', 'number': 10, 's_plus_number': 2},
    star_rank                   = db.Column(db.Integer)
    weapon_paint_point          = db.Column(db.Integer)
    game_paint_point            = db.Column(db.Integer) # 塗りポイント
    rank                        = db.Column(db.Integer) # ランク
    kill_count                  = db.Column(db.Integer) # キル数
    assist_count                = db.Column(db.Integer) # キルアシスト数
    death_count                 = db.Column(db.Integer) # デス数
    special_count               = db.Column(db.Integer) # スペシャル発動数
    sort_score                  = db.Column(db.Integer)
    # player: {shoes, shoes_skills, weapon, head_skills, nickname, principal_id, head, clothes, clothes_skills, star_rank}
    team                        = db.Column(db.String, nullable=False) # my or other

    @property
    def udemae_text(self):
        name = self.udemae['name']
        num = self.udemae['s_plus_number']
        return name + num
