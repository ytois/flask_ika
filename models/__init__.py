from flask import current_app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(current_app)

from models.user import User
from models.switch_session import SwitchSession
from models.stage import Stage
from models.game_mode import GameMode
from models.rule import Rule
from models.team_result import TeamResult
from models.schedule import Schedule
from models.battle_result import BattleResult
from models.battle_member import BattleMember
