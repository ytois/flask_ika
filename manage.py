from app import app
from flask_script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from models import db


manager = Manager(app.app)

migrate = Migrate(app.app, db)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
