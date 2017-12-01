from app import app
from utils.slack_notifer import SlackNotifer
from flask import request


# TODO: とりあえず
@app.errorhandler(Exception)
def error_unknown(e):
    SlackNotifer().error_notify(e, request)
    return "Internal Server Error"

# @app.errorhandler(400)
# @app.errorhandler(401)
# @app.errorhandler(404)
# @app.errorhandler(405)
# @app.errorhandler(409)
# @app.errorhandler(500)
# def error(e):
#     pass
