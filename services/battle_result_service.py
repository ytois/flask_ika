from models import db, BattleResult, Stage, Rule, GameMode, TeamResult
from utils.splatoon_api import SplatoonApi


class BattleResultService:

    def __init__(self, user):
        self.user = user
        self.__api = SplatoonApi(user.iksm_session)

    def fetch_results(self):
        raw_results = self.__api.results()
        if not raw_results:
            return []

        battle_numbers = [r['battle_number'] for r in raw_results['results']]

        # 既に保存済みのナンバーを取得して除外する
        exist_battles = BattleResult.query.filter(
            BattleResult.battle_number.in_(battle_numbers),
            BattleResult.user_id == self.user.id
        )

        for exist_battle in exist_battles:
            battle_numbers.remove(exist_battle.battle_number)

        # apiからdictを返却
        return [self.__api.results(n) for n in battle_numbers]

    def save_results(self):
        results = self.fetch_results()
        for result in results:
            BattleResultBuilder(result).save()


class BattleResultBuilder:
    def __init__(self, _dict, user):
        self.user = user
        self.__raw = _dict
        for key in self.__loadattr_keys:
            if key in _dict:
                setattr(self, key, _dict[key])

    def save(self):
        battle_result = self.build_result()
        db.session.add(battle_result)
        db.session.commit()

    def build(self):
        with db.session.no_autoflush:
            battle_result = BattleResult()

            for attr in self.__setattr_keys:
                if attr in dir(self):
                    value = self.__getattribute__(attr)
                else:
                    value = None
                battle_result.__setattr__(attr, value)

        # member,playerはBattleMemberBuilderのインスタンスが返される
        # それぞれbuildしてBattleMemberインスタンスを作る

        # TODO: build処理実装する
        # battle_result.player = self.player.build()
        #
        # for member in self.members:
        #     battle_result.members.append(member.build())

        return battle_result

    @property
    def stage(self):
        stage = Stage.query.filter_by(stage_id = int(self.__raw['stage']['id'])).first()
        if stage:
            return stage
        else:
            # 存在しない場合はDBに保存する
            stage = Stage.save_from_dict(self.__raw['stage'])
            return stage

    @property
    def rule(self):
        return Rule.query.filter_by(name_en = self.__raw['rule']['key']).first()

    @property
    def game_mode(self):
        return GameMode.query.filter_by(name_en = self.__raw['game_mode']['key']).first()

    @property
    def my_team_result(self):
        key = self.__raw['my_team_result']['key']
        return TeamResult.query.filter_by(key = key).first()

    @property
    def other_team_result(self):
        key = self.__raw['other_team_result']['key']
        return TeamResult.query.filter_by(key = key).first()

    @property
    def player(self):
        return BattleMemberBuilder(self.__raw['player_result'], 'my_team')

    @property
    def members(self):
        my_team = [BattleMemberBuilder(m, 'my_team') for m in self.my_team_members]
        other_team = [BattleMemberBuilder(m, 'other_team') for m in self.other_team_members]
        return my_team + other_team

    @property
    def my_team_members(self):
        # ユーザー自信は除外する
        members = []
        user_principal_id = self.__raw['player_result']['player']['principal_id']

        for member in self.__raw['my_team_members']:
            member_principal_id = member['player']['principal_id']
            if not user_principal_id == member_principal_id:
                members.append(member)

        return members

    @property
    def other_team_members(self):
        return self.__raw['other_team_members']

    @property
    def __loadattr_keys(self):
        return [
            'battle_number',
            'my_team_percentage',
            'other_team_percentage',
            'player_rank',
            'star_rank',
            'start_time',
            'weapon_paint_point',
            'win_meter'
        ]

    @property
    def __setattr_keys(self):
        return [
            'battle_number',
            'user',
            'stage',
            'rule',
            'game_mode',
            'elpased_time',
            'my_team_result',
            'other_team_result',
            'estimate_gachi_power',
            'my_team_count',
            'other_team_count',
            'league_point',
            'max_league_point',
            'my_estimate_league_point',
            'other_estimate_league_point',
            'win_meter',
            'my_team_percentage',
            'other_team_percentage',
        ]


class BattleMemberBuilder:
    def __init__(self, _dict, team):
        self.__raw = _dict
        self.__raw_player = _dict['player']
        self.team = team

        for key in self.__setattr_keys:
            if key in _dict:
                setattr(self, key, _dict[key])
            else:
                setattr(self, key, None)

        for key in self.__setattr_player_keys:
            if key in _dict['player']:
                setattr(self, key, _dict['player'][key])
            else:
                setattr(self, key, None)
    @property
    def gears(self):
        ['weapon', 'shoes', 'head_skills',
         'clothes', 'shoes_skills', 'head', 'clothes_skills']

    @property
    def __setattr_keys(self):
        return ['assist_count', 'death_count', 'sort_score', 'game_paint_point', 'special_count', 'kill_count']

    @property
    def __setattr_player_keys(self):
        return ['player_rank', 'star_rank', 'nickname', 'principal_id', 'udemae']
