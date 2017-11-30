from flask import current_app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(current_app)

from models.user import User
from models.switch_session import SwitchSession
