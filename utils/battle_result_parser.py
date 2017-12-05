from models import BattleResult
from datetime import datetime


class BattleResultPaser:
    def __init__(self, unique_battle_id, _dict):
        self.unique_battle_id
        self.__raw

        for key in self.__setattr_keys:
            setattr(self, key, self.__raw[key])

    def save(self):
        self.__save_battle_result()

    @property
    def stage_id(self):
        pass

    @property
    def rule_id(self):
        pass

    @property
    def game_mode_id(self):
        pass

    @property
    def start_date(self):
        unix_time = int(self.__raw['start_time'])
        return datetime.fromtimestamp(unix_time)


    @property
    def udemae(self):
        pass

    @property
    def player_kill_count(self):
        pass

    @property
    def player_assist_count(self):
        pass

    @property
    def player_death_count(self):
        pass

    @property
    def player_special_count(self):
        pass

    @property
    def player_game_paint_point(self):
        pass

    @property
    def player_sort_score(self):
        pass

    @property
    def my_team_result_id(self):
        pass

    @property
    def other_team_result_id(self):
        pass

    @property
    def __setattr_keys(self):
        return [
            'battle_number',
            'elpased_time',
            'estimate_gachi_power',
            'league_point',
            'max_league_point',
            'player_rank',
            'star_rank',
            'tag_id',
            'weapon_paint_point',
            'my_estimate_league_point',
            'my_team_count',
            'other_estimate_league_point',
            'other_team_count',
        ]

    def __save_battle_result(self):
        result = BattleResult()
        return result.add().commit()

    # def __save_players(self):
    #     pass
