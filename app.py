# my-lair-a > app.py

from flask import Flask,  request
from models.slack import SlackManager
app = Flask(__name__)

slack = SlackManager()


@app.route('/')
def index():
    return "Welcome to the Slack Microservice", 200


# Sample body {"channel_id: "CXXXXXX", "message": "Hello world :tada:"}
@app.post('/message')
def post_message():
    print("Request", request.json)
    slack.client.chat_postMessage(
        channel=request.json["channel_id"],
        text=request.json["message"]
    )
    return "Message successfully posted to channel", 200


@app.route('/channels')
def get_channels():
    response = slack.client.conversations_list()
    channels = [(x['id'], x['name']) for x in response['channels']]
    return channels, 200


if __name__ == '__main__':
    app.run()
