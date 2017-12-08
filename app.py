from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_jsglue import JSGlue
import flask.ext.color
import os


class Application:
    def __init__(self):
        self.app = Flask(__name__, instance_relative_config=True)
        self.configure()
        self.set_template_engine()
        self.activate_color()
        self.set_csrf()
        self.setup_extention()

    # load config
    def configure(self):
        self.app.config['SECRET_KEY'] = os.urandom(24)
        self.app.config.from_object('config.default')

        if os.getenv('FLASK_ENV', 'development') == 'production':
            self.app.config.from_object('config.production')
        else:
            self.app.config.from_object('config.development')

        # instanceからローカル設定の読み込み
        self.app.config.from_pyfile('config.py')
        # current_appで'Working outside of application context'が出る対策。ようわからん。
        self.app.app_context().push()

        self.app.config['SQLALCHEMY_DATABASE_URI'] = self.db_uri

    def set_template_engine(self):
        # use template jade
        self.app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

    def activate_color(self):
        flask.ext.color.init_app(self.app)

    def set_csrf(self):
        self.csrf = CSRFProtect(self.app)

    def setup_extention(self):
        jsglue = JSGlue(self.app)

    @property
    def db_uri(self):
        db_config = self.app.config['DATABASE']
        user = db_config['user']
        passwd = db_config['pass']
        host = db_config['host']
        db = db_config['db']
        port = 5432

        return 'postgresql://{user}{password}@{host}:{port}/{db}'.format(
            user=user,
            password=':%s' % passwd if passwd else '',
            host=host,
            db=db,
            port=port,
        )

app = Application().app

# TODO: 暫定でclass外に置く
login_manager = LoginManager()
login_manager.init_app(app)

from models import User
from views import routing


@login_manager.user_loader
def user_loader(id):
    return User.query.get(id)


if __name__ == '__main__':
    app.run()
