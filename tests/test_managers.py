import pytest
from unittest.mock import Mock
from slack_sdk.errors import SlackApiError
from managers.slack_manager import SlackManager, SlackManagerError

slack_manager = SlackManager()
slack_manager.client = Mock()


def test_slack_manager_get_channel_list():
    slack_manager.client.conversations_list.return_value = {
        "channels": [
            {"id": "C2312", "name": "random ", "other data": "lorem ipsum"},
            {"id": "C5312", "name": "general "},
        ]
    }
    assert slack_manager.get_channel_list() == [
        ("C2312", "random "),
        ("C5312", "general "),
    ]

    with pytest.raises(SlackManagerError) as e_info:
        slack_manager.client.conversations_list.side_effect = SlackApiError(
            "slack exception", {"error": "not_authed"}
        )
        slack_manager.get_channel_list()

    slack_manager.client.chat_postMessage.return_value = ""
    slack_manager.send_message("test_id", "test_message")
    slack_manager.client.chat_postMessage.assert_called_once()


def test_slack_manager_send_message():
    with pytest.raises(SlackManagerError) as e_info:
        slack_manager.client.chat_postMessage.side_effect = SlackApiError(
            "slack exception", {"error": "not_authed"}
        )
        slack_manager.send_message("test_id", "test_message")
