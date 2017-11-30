from flask_classy import FlaskView, route
from flask import render_template, redirect, session, request
from utils.twitter_oauth import TwitterOauth


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
        access_token, access_token_secret = twitter.fetch_access_token(
            request.args.get('oauth_token'),
            session.get('request_token_secret'),
            request.args.get('oauth_verifier')
        )

        session.pop('request_token_secret', None)
        session.pop('request_token', None)

        # TODO: ユーザーに保存する
        return render_template("frontend/top/callback.jade", access_token=access_token, access_token_secret=access_token_secret)
