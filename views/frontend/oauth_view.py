from flask_classy import FlaskView, route
from flask import render_template, redirect, session, request, flash
from utils.twitter_oauth import TwitterOauth
from flask_login import login_user
from models import User


class OauthView(FlaskView):
    route_base = '/oauth/'

    # /oauth/twitter
    def twitter(self):
        twitter = TwitterOauth()
        token, secret, url = twitter.request_parmas()

        # callback先で使うのでsessionに保存しておく
        session['request_token'] = token
        session['request_token_secret'] = secret

        return redirect(url)

    # /oauth/twitter/callback
    @route('/twitter/callback')
    def twitter_callback(self):
        twitter = TwitterOauth()
        user_infomation = twitter.fetch_access_token(
            request.args.get('oauth_token'),
            session.get('request_token_secret'),
            request.args.get('oauth_verifier')
        )

        # セッションから削除
        session.pop('request_token_secret', None)
        session.pop('request_token', None)

        user = User.query.filter_by(twitter_user_id=user_infomation['twitter_user_id']).first()

        if user:
            # 既存ユーザー
            flash("ログインしました")
        else:
            # 新規ユーザーを登録
            user = User(
                screen_name=user_infomation['screen_name'],
                twitter_user_id=user_infomation['twitter_user_id'],
                access_token=user_infomation['access_token'],
                access_token_secret=user_infomation['access_token_secret']
            )
            user.add().commit()
            flash("登録しました")

        # login情報の保存
        login_user(user, True)

        return redirect('/')
