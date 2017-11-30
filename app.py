from flask import Flask
import flask.ext.color
import os


class Application:
    def __init__(self):
        self.app = Flask(__name__, instance_relative_config=True)
        self.configure()
        self.set_template_engine()
        self.activate_color()

    # load config
    def configure(self):
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


app = Application().app

from views.frontend.top_view import TopView
TopView.register(app)

if __name__ == '__main__':
    app.run()
