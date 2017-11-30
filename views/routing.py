from app import app

# /
from views.frontend.top_view import TopView
TopView.register(app.app)

# /oauth/
from views.frontend.oauth_view import OauthView
OauthView.register(app.app)

# /setting/
from views.frontend.setting_view import SettingView
SettingView.register(app.app)

# /api/
from views.api.api_view import ApiView
ApiView.register(app.app)
