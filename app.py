from flask import Flask
from flask_wtf.csrf import CSRFProtect
import flask.ext.color
import os


class Application:
    def __init__(self):
        self.app = Flask(__name__, instance_relative_config=True)
        self.configure()
        self.set_template_engine()
        self.activate_color()
        self.set_csrf()

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

    def set_template_engine(self):
        # use template jade
        self.app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

    def activate_color(self):
        flask.ext.color.init_app(self.app)

    def set_csrf(self):
        self.csrf = CSRFProtect(self.app)


app = Application().app

# route: /
from views.frontend.top_view import TopView
TopView.register(app)

# route: /api/
from views.api.api_view import ApiView
ApiView.register(app)

# route: /oauth/
from views.frontend.oauth_view import OauthView
OauthView.register(app)

if __name__ == '__main__':
    app.run()
