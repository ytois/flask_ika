from models import db


# 中間テーブル
battle_result_members = db.Table(
    'battle_result_members',
    db.metadata,
    db.Column('battle_result_id', db.Integer, db.ForeignKey('battle_results.id')),
    db.Column('battle_member_id', db.Integer, db.ForeignKey('battle_members.id'))
)
