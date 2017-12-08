from models import db, BattleResult, Stage, Rule, GameMode, TeamResult, BattleMember
from utils.splatoon_api import SplatoonApi
from datetime import datetime


class BattleResultService:

    def __init__(self, user):
        self.user = user
        self._api = SplatoonApi(user.iksm_session)
        self.exists_record_update = False  # 既に登録済みの場合上書きするか

    def fetch_results(self):
        raw_results = self._api.results()
        if not raw_results:
            return []
        results = raw_results['results']

        if not self.exists_record_update:
            battle_numbers = [r['battle_number'] for r in results]

            # 既に保存済みのナンバーを取得
            exist_battles = BattleResult.query.filter(
                BattleResult.battle_number.in_(battle_numbers),
                BattleResult.user_id == self.user.id
            )
            exist_battle_numbers = [r.battle_number for r in exist_battles]

            # 除外する
            for result in results:
                if result['battle_number'] in exist_battle_numbers:
                    results.remove(result)

        # apiからdictを返却
        return results

    def save_results(self):
        response = []
        results = self.fetch_results()

        for result in results:
            result_detail = self._api.results(result['battle_number'])
            response.append(BattleResultBuilder(result_detail, self.user).save())
            print('[save] battle_number: %s' % result['battle_number'])

        return response


class BattleResultBuilder:
    def __init__(self, _dict, user):
        self.user = user
        self._raw = _dict
        for key in self._loadattr_keys:
            if key in _dict:
                setattr(self, key, _dict[key])

    def save(self):
        battle_result = self.build()
        db.session.add(battle_result)
        db.session.commit()
        return battle_result

    def build(self):
        with db.session.no_autoflush:
            # 既に登録済みならupdate
            battle_result = BattleResult.query.filter_by(
                user_id=self.user.id, battle_number=self.battle_number
            ).first()

            # 無ければcreate
            if not battle_result:
                battle_result = BattleResult()

            for attr in self._setattr_keys:
                if attr in dir(self):
                    value = self.__getattribute__(attr)
                else:
                    value = None
                battle_result.__setattr__(attr, value)

        # member,playerはBattleMemberBuilderのインスタンスが返される
        # それぞれbuildしてBattleMemberインスタンスを作る
        battle_result.player = self.player.build()

        for member in self.members:
            battle_result.members.append(member.build())

        return battle_result

    @property
    def start_time(self):
        return datetime.fromtimestamp(self._raw['start_time'])

    @property
    def stage(self):
        stage = Stage.query.filter_by(stage_id = int(self._raw['stage']['id'])).first()
        if stage:
            return stage
        else:
            # 存在しない場合はDBに保存する
            stage = Stage.save_from_dict(self._raw['stage'])
            return stage

    @property
    def rule(self):
        return Rule.query.filter_by(name_en = self._raw['rule']['key']).first()

    @property
    def game_mode(self):
        return GameMode.query.filter_by(name_en = self._raw['game_mode']['key']).first()

    @property
    def my_team_result(self):
        key = self._raw['my_team_result']['key']
        return TeamResult.query.filter_by(key = key).first()

    @property
    def other_team_result(self):
        key = self._raw['other_team_result']['key']
        return TeamResult.query.filter_by(key = key).first()

    @property
    def player(self):
        return BattleMemberBuilder(self._raw['player_result'], 'my_team')

    @property
    def members(self):
        my_team = [BattleMemberBuilder(m, 'my_team') for m in self.my_team_members]
        other_team = [BattleMemberBuilder(m, 'other_team') for m in self.other_team_members]
        return my_team + other_team

    @property
    def my_team_members(self):
        # ユーザー自信は除外する
        members = []
        user_principal_id = self._raw['player_result']['player']['principal_id']

        for member in self._raw['my_team_members']:
            member_principal_id = member['player']['principal_id']
            if not user_principal_id == member_principal_id:
                members.append(member)

        return members

    @property
    def other_team_members(self):
        return self._raw['other_team_members']

    @property
    def _loadattr_keys(self):
        return [
            'battle_number',
            'my_team_percentage',
            'other_team_percentage',
            'player_rank',
            'elapsed_time',
            'weapon_paint_point',
            'win_meter',
            'estimate_gachi_power',
            'my_team_count',
            'other_team_count',
            'league_point',
            'max_league_point',
            'my_estimate_league_point',
            'other_estimate_league_point',
        ]

    @property
    def _setattr_keys(self):
        return [
            'battle_number',
            'user',
            'stage',
            'rule',
            'game_mode',
            'start_time',
            'elapsed_time',
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
        self._raw = _dict
        self._raw_player = _dict['player']
        self.team = team

        for key in self._setattr_keys:
            if key in _dict:
                setattr(self, key, _dict[key])
            else:
                setattr(self, key, None)

        for key in self._setattr_player_keys:
            if key in _dict['player']:
                setattr(self, key, _dict['player'][key])
            else:
                setattr(self, key, None)

    def build(self):
        with db.session.no_autoflush:
            member = BattleMember(team=self.team)

            for attr in self._setattr_keys + self._setattr_player_keys:
                if attr in dir(self):
                    value = self.__getattribute__(attr)
                else:
                    value = None
                member.__setattr__(attr, value)

        return member

    @property
    def gears(self):
        ['weapon', 'shoes', 'head_skills',
         'clothes', 'shoes_skills', 'head', 'clothes_skills']

    @property
    def _setattr_keys(self):
        return ['assist_count', 'death_count', 'sort_score', 'game_paint_point', 'special_count', 'kill_count']

    @property
    def _setattr_player_keys(self):
        return ['player_rank', 'star_rank', 'nickname', 'principal_id', 'udemae']
