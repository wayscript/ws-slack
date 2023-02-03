from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os


class SlackManager:
    def __init__(self) -> None:
        self.client = WebClient(os.getenv('SLACK_API_TOKEN'))
