import pytest
from unittest.mock import patch, Mock
from managers.slack_manager import SlackManager, SlackManagerError
from slack_sdk.errors import SlackApiError


def test_slack_manager():
    slack_manager = SlackManager()
    slack_manager.client = Mock()
    slack_manager.client.conversations_list.return_value = {"channels": [
        {"id": "C2312", "name": "random ", "other data": "lorem ipsum"},
        {"id": "C5312", "name": "general "}
    ]}
    assert slack_manager.get_channel_list() == [(
        'C2312', 'random '), ('C5312', 'general ')]

    with pytest.raises(SlackManagerError) as e_info:
        slack_manager.client.conversations_list.side_effect = SlackApiError(
            "slack exception", {"error": 'not_authed'})
        slack_manager.get_channel_list()

    slack_manager.client.chat_postMessage.return_value = ''
    slack_manager.send_message("test_id", "test_message")
    slack_manager.client.chat_postMessage.assert_called_once()

    with pytest.raises(SlackManagerError) as e_info:
        slack_manager.client.chat_postMessage.side_effect = SlackApiError(
            "slack exception", {"error": 'not_authed'})
        slack_manager.send_message("test_id", "test_message")
