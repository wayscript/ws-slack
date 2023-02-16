import pytest, json
from unittest.mock import Mock
from app import create_app
from managers.slack_manager import SlackManagerError


@pytest.fixture()
def app():
    app = create_app()
    yield app


@pytest.mark.parametrize(
    " error, expected_response",
    [
        ("", {"status": "Slack API is connected and working properly"}),
        (
            SlackManagerError("test_error"),
            {"error": "Slack exception ocurred: test_error"},
        ),
    ],
)
def test_get_status(app, error, expected_response):
    slack_manager = Mock()
    app.config["SlackManager"] = slack_manager
    sample_channels = [
        ["CB8886H7V", "random"],
        ["CB98179M4", "general"],
        ["CEQ4SQQAF", "blog_posts"],
    ]
    slack_manager.get_channel_list.return_value = sample_channels
    if error:
        slack_manager.get_channel_list.side_effect = error

    response = app.test_client().get("/status")

    assert json.loads(response.data.decode()) == expected_response


@pytest.mark.parametrize(
    "channels, error, expected_response",
    [
        (
            [
                ["CB8886H7V", "random"],
                ["CB98179M4", "general"],
                ["CEQ4SQQAF", "blog_posts"],
            ],
            "",
            [
                ["CB8886H7V", "random"],
                ["CB98179M4", "general"],
                ["CEQ4SQQAF", "blog_posts"],
            ],
        ),
        (
            [
                ["CB8886H7V", "random"],
                ["CB98179M4", "general"],
                ["CEQ4SQQAF", "blog_posts"],
            ],
            SlackManagerError("test_error"),
            {"error": "Slack exception ocurred: test_error"},
        ),
    ],
)
def test_get_channels(app, channels, error, expected_response):
    slack_manager = Mock()
    app.config["SlackManager"] = slack_manager
    slack_manager.get_channel_list.return_value = channels
    if error:
        slack_manager.get_channel_list.side_effect = error

    response = app.test_client().get("/channels")

    assert json.loads(response.data.decode()) == expected_response


@pytest.mark.parametrize(
    "params, error, expected_response",
    [
        (
            {"message": "hello world", "target_id": "CXXXXX"},
            "",
            {"message": "Message successfully posted to channel"},
        ),
        (
            {"message": "hello world", "target_id": "CXXXXX"},
            SlackManagerError("test_error"),
            {"error": "Slack exception ocurred: test_error"},
        ),
        (
            {"message": "test message"},
            "",
            {"error": "Required parameters not present"},
        ),
        (
            {"message": "test message"},
            SlackManagerError("test_error"),
            {"error": "Required parameters not present"},
        ),
    ],
)
def test_post_message(app, params, error, expected_response):
    slack_manager = Mock()
    app.config["SlackManager"] = slack_manager
    slack_manager.send_message.return_value = {
        "message": "Message successfully posted to channel"
    }
    if error:
        slack_manager.send_message.side_effect = SlackManagerError("test_error")

    response = app.test_client().post("/message", json=params)

    assert json.loads(response.data.decode()) == expected_response
