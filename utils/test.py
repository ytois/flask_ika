from models import db, BattleResult, BattleMember
from datetime import datetime


def insert_test():
    members = [
        BattleMember(principal_id='a1', team='my'),
        BattleMember(principal_id='b1', team='my'),
        BattleMember(principal_id='c1', team='other'),
        BattleMember(principal_id='d1', team='other'),
    ]

    result = BattleResult(
        user_id=1,
        battle_number=999,
        stage_id=1,
        rule_id=1,
        game_mode_id=1,
        start_time=datetime.now(),
        elpased_time=30,
        my_team_result_id=1,
        other_team_result_id=2,
    )

    result.player = members[0]

    for m in members[1:]:
        result.members.append(m)

    db.session.add(result)
    db.session.commit()
