# my-lair-a > app.py

from flask import Flask,  request
from managers.slack_manager import SlackManager, SlackManagerError
app = Flask(__name__)

slack = SlackManager()


@app.route('/')
def index():
    return "Welcome to the Slack Microservice", 200


# Sample body {"target_id: "CXXXXXX", "message": "Hello world :tada:"}
@app.post('/message')
def post_message():
    if "target_id" in request.json and "message" in request.json:
        try:
            slack.send_message(
                request.json['target_id'], request.json['message'])
        except SlackManagerError as e:
            return str(e), e.error_code
    else:
        return "Required parameters not present", 400

    return "Message successfully posted to channel", 200


@app.get('/status')
def get_status():
    try:
        slack.get_channel_list()
    except SlackManagerError as e:
        return str(e), e.error_code
    return "Slack API is connected and working properly", 200


@app.route('/channels')
def get_channels():
    try:
        channels = slack.get_channel_list()
    except SlackManagerError as e:
        return str(e), e.error_code

    return channels, 200


if __name__ == '__main__':
    app.run()
