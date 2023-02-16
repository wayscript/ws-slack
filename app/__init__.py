from flask import Flask, request
from managers.slack_manager import SlackManager, SlackManagerError


def create_app(slack_manager=SlackManager()):
    app = Flask(__name__)
    app.config["SlackManager"] = slack_manager

    @app.route("/")
    def index():
        slack = app.config["SlackManager"]
        return "Welcome to the Slack Microservice", 200

    # Sample body {"target_id: "CXXXXXX", "message": "Hello world :tada:"}
    @app.post("/message")
    def post_message():
        slack = app.config["SlackManager"]
        if "target_id" in request.json and "message" in request.json:
            try:
                slack.send_message(request.json["target_id"], request.json["message"])
            except SlackManagerError as e:
                return {"error": str(e)}, e.error_code
        else:
            return {"error": "Required parameters not present"}, 400

        return {"message": "Message successfully posted to channel"}, 200

    @app.get("/status")
    def get_status():
        slack = app.config["SlackManager"]
        try:
            slack.get_channel_list()
        except SlackManagerError as e:
            return {"error": str(e)}, e.error_code
        return {"status": "Slack API is connected and working properly"}, 200

    @app.route("/channels")
    def get_channels():
        slack = app.config["SlackManager"]
        try:
            channels = slack.get_channel_list()
        except SlackManagerError as e:
            return {"error": str(e)}, e.error_code

        return channels, 200

    return app
