from app import app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import db
from commands.seed import Seed


manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
manager.add_command('seed', Seed)

if __name__ == "__main__":
    manager.run()
