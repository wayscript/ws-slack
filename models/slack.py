from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os


class SlackManager:
    def __init__(self) -> None:
        self.client = WebClient(os.getenv('SLACK_API_TOKEN'))

    def handle_slack_exception(self, slack_error_msg):
        if slack_error_msg == 'not_authed':
            raise SlackManagerError("Slack API Key is not set", error_code=500)
        elif slack_error_msg == ' invalid_auth':
            raise SlackManagerError("Slack API Key is invalid", error_code=500)
        elif slack_error_msg == 'channel_not_found':
            raise SlackManagerError(
                "The channel to which the message was requested to be sent to does not exist", error_code=400)
        else:
            print("Unhandled exception ocurred: ", slack_error_msg)
            raise SlackManagerError(
                "Unknown error ocurred, please contact the administrator", error_code=500)

    def get_channel_list(self):
        try:
            response = self.client.conversations_list()
            channels = [(x['id'], x['name']) for x in response['channels']]
            return channels
        except SlackApiError as e:
            print(type(e.response['error']))
            self.handle_slack_exception(e.response['error'])

    def send_message(self, target_id, message):
        try:
            self.client.chat_postMessage(
                channel=target_id,
                text=message
            )
        except SlackApiError as e:
            self.handle_slack_exception(e.response['error'])


class SlackManagerError(Exception):
    def __init__(self, message='', error_code=500) -> None:
        self.message = f"Slack exception ocurred: {message}"
        self.error_code = error_code
        super().__init__(self.message)
