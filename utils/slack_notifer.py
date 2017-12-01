from slackweb import Slack
from flask import current_app
import traceback


class SlackNotifer:
    def __init__(self, channel_url=None):
        self.channel = channel_url or current_app.config['SLACK_NOTIFICATION']

    def error_notify(self, e, request=None):
        attachments = []

        class_name = e.__class__.__name__
        message = str(e)
        stack_trace = traceback.format_exc()

        attachment = {
            'color': 'danger',
            'pretext': 'flask-ika: raise error',
            'title': class_name,
            'fields': [
                {'title': 'method', 'value': request.method},
                {'title': 'url', 'value': request.url},
                {'title': 'params', 'value': str(dict(request.args))},
                {'title': 'message', 'value': message},
                {'title': 'stack trace', 'value': stack_trace},
            ]
        }

        attachments.append(attachment)
        return self.__notify(attachments=attachments)

    def __notify(self, text=None, attachments=None):
        return Slack(url=self.channel).notify(text=text, attachments=attachments)
