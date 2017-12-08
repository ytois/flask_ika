from models import db
from datetime import datetime


class BattleMember(db.Model):
    __tablename__ = 'battle_members'

    id                 = db.Column(db.Integer, primary_key=True)
    created_at         = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at         = db.Column(db.DateTime, onupdate=datetime.utcnow)

    team               = db.Column(db.String, nullable=False) # my or other
    principal_id       = db.Column(db.String, nullable=False) # principal_id
    nickname           = db.Column(db.String, nullable=False)
    star_rank          = db.Column(db.Integer)
    weapon_paint_point = db.Column(db.Integer) # 武器塗りポイント
    game_paint_point   = db.Column(db.Integer) # 塗りポイント
    player_rank        = db.Column(db.Integer) # ランク
    kill_count         = db.Column(db.Integer) # キル数
    assist_count       = db.Column(db.Integer) # キルアシスト数
    death_count        = db.Column(db.Integer) # デス数
    special_count      = db.Column(db.Integer) # スペシャル発動数
    sort_score         = db.Column(db.Integer)
    # player: {shoes, shoes_skills, weapon, head_skills, nickname, principal_id, head, clothes, clothes_skills, star_rank}

    # ガチ/リーグのみ
    udemae             = db.Column(db.JSON)
    # udemae ex. {'is_number_reached': False, 'name': 'S+', 'number': 10, 's_plus_number': 2},

    # relation
    # gears

    @property
    def udemae_text(self):
        if not self.udemae:
            return None

        name = self.udemae['name']
        num = self.udemae['s_plus_number']
        return '%s%s' % (name, num)

    def to_dict(self):
        response = {}
        keys = ['team', 'nickname', 'star_rank',
                'weapon_paint_point', 'game_paint_point',
                'player_rank', 'kill_count', 'assist_count',
                'death_count', 'special_count', 'sort_score',]

        for key in keys:
            value = self.__getattribute__(key)
            response[key] = value

        response['udemae'] = self.udemae_text
        # response['udemae_meter'] = self.udemae['number']

        return response
