from app import app

# /
from views.frontend.top_view import TopView
TopView.register(app)

# /oauth/
from views.frontend.oauth_view import OauthView
OauthView.register(app)

# /setting/
from views.frontend.setting_view import SettingView
SettingView.register(app)

# /api/
from views.api.api_view import ApiView
ApiView.register(app)

# error page
if not app.debug:
    from views.frontend import error_view
