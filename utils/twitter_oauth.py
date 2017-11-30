from flask import current_app
from rauth import OAuth1Service
from IPython import embed


class TwitterOauth:
    CALLBACK_URL = 'http://localhost:5000/oauth/twitter/callback'

    def __init__(self, consumer_key=None, consumer_secret=None):
        self.consumer_key = consumer_key or current_app.config['TWITTER_CONSUMER_KEY']
        self.consumer_secret = consumer_secret or current_app.config['TWITTER_CONSUMER_SECRET']

    @property
    def service(self):
        return OAuth1Service(
            name='twitter',
            consumer_key=self.consumer_key,
            consumer_secret=self.consumer_secret,
            request_token_url='https://api.twitter.com/oauth/request_token',
            access_token_url='https://api.twitter.com/oauth/access_token',
            authorize_url='https://api.twitter.com/oauth/authorize',
            base_url='https://api.twitter.com/1.1/'
        )

    def request_parmas(self):
        """
        コールバック先にoauth_token, oauth_verifierがついて返ってくる
        """
        request_token, request_token_secret = self.service.get_request_token(
            params={'oauth_callback': self.CALLBACK_URL}
        )
        authorize_url = self.service.get_authorize_url(request_token)
        return (request_token, request_token_secret, authorize_url)

    def fetch_access_token(self, oauth_token, request_token_secret, oauth_verifier):
        """
        access_tokenとaccess_token_secretを返す
        """
        self.session = self.service.get_auth_session(
            oauth_token,
            request_token_secret,
            data={'oauth_verifier': oauth_verifier}
        )

        end_point = 'https://api.twitter.com/1.1/account/verify_credentials.json'
        response = self.session.get(end_point)

        if response.status_code == 200:
            user_data = response.json()
        else:
            pass

        return {
            'access_token': self.session.access_token,
            'access_token_secret': self.session.access_token_secret,
            'twitter_user_id': user_data['id'],
            'screen_name': user_data['screen_name']
        }
