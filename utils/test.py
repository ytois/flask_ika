from models import db, BattleResult, BattleMember
from datetime import datetime


def insert_test():
    members = [
        BattleMember(principal_id='a1'),
        BattleMember(principal_id='b1'),
        BattleMember(principal_id='c1'),
        BattleMember(principal_id='d1'),
    ]

    result = BattleResult(
        battle_number=999,
        stage_id=1,
        rule_id=1,
        game_mode_id=1,
        start_time=datetime.now(),
        end_time=datetime.now(),
        my_team_result_id=1,
        other_team_result_id=2,
    )

    result.player = members[0]

    for m in members[1:]:
        result.members.add(m)

    db.session.add(result)
    db.session.commit()
