import pytest, json
from unittest.mock import Mock
from app import create_app
from managers.slack_manager import SlackManagerError


@pytest.fixture()
def app():
    app = create_app()
    yield app


def test_get_channels_status(app):
    slack_manager = Mock()
    app.config["SlackManager"] = slack_manager
    sample_channels = [
        ["CB8886H7V", "random"],
        ["CB98179M4", "general"],
        ["CEQ4SQQAF", "blog_posts"],
    ]
    slack_manager.get_channel_list.return_value = sample_channels
    response = app.test_client().get("/channels")
    assert json.loads(response.data.decode()) == sample_channels

    response = app.test_client().get("/status")
    assert json.loads(response.data.decode()) == {
        "status": "Slack API is connected and working properly"
    }

    slack_manager.get_channel_list.side_effect = SlackManagerError("test_error")
    response = app.test_client().get("/channels")
    assert json.loads(response.data.decode()) == {
        "error": "Slack exception ocurred: test_error"
    }

    response = app.test_client().get("/status")
    assert json.loads(response.data.decode()) == {
        "error": "Slack exception ocurred: test_error"
    }


successful_message_sent_response = {"message": "Message successfully posted to channel"}
incorrect_params_response = {"error": "Required parameters not present"}


@pytest.mark.parametrize(
    "params, expected_response",
    [
        (
            {"message": "hello world", "target_id": "CXXXXX"},
            successful_message_sent_response,
        ),
        ({"message": "test message"}, incorrect_params_response),
    ],
)
def test_post_message(app, params, expected_response):
    slack_manager = Mock()
    app.config["SlackManager"] = slack_manager
    slack_manager.send_message.return_value = successful_message_sent_response
    response = app.test_client().post("/message", json=params)
    assert json.loads(response.data.decode()) == expected_response

    # response = app.test_client().post(
    #     "/message",
    #     json={
    #         "message": "Hello world",
    #     },
    # )
    # assert json.loads(response.data.decode()) == incorrect_params_response

    slack_manager.send_message.side_effect = SlackManagerError("test_error")
    response = app.test_client().post(
        "/message", json={"message": "Hello world", "target_id": "CXXXX"}
    )
    assert json.loads(response.data.decode()) == {
        "error": "Slack exception ocurred: test_error"
    }
