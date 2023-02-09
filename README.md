![img](https://i.ibb.co/Vgv9nf1/interface3.png)

# Spin Up a Slack Microservice using Flask

This template is an example of a web server inside the WayScript X lair environment that can query the Slack API. It includes 3 endpoints -

- `GET /channels` - get all the channels in a workspace
- `POST /message` send message to a channel or user
- `GET /status` checks whether the API is properly integrated with slack

## Setup

### 1) Setup a Slack App

In order to setup a slack app, complete the following tutorials.

- [Create an app](https://api.slack.com/authentication/basics#creating)
- [Request scopes](https://api.slack.com/authentication/basics#scopes) - Scopes dictate how much power your slack app posessess. In the sidebar of your app page, click on "OAuth & Permissions" and scroll down to the Scopes section. Add the following scopes `channels:read`, `chat:write`, `chat:write.public`.
- [Install to a workspace of your choice](https://api.slack.com/authentication/basics#installing) - Click on the "Install App" button in the sidebar of your app page. Click on the "Install App To Workspace" to install to your workspace.

### 2) Save auth token to Lair

Open the OAuth & Permissions section from the app sidebar. It's the same place you setup the app scopes. Copy the `Bot User OAuth Token`.

Next, save the key to the [`.secrets`](https://docs.wayscript.com/platform/lairs/environment-variables#example-.env-and-.secrets-files) file in your Lair. Set the `key` as `SLACK_API_TOKEN` and the `value` as the token you obtained from slack.

### 3) Verify that service is up and working correctly

Visit the `/status` endpoint. If you get "Slack API is connected and working properly", it means the service is running and authenticated to connect with your slack workspace. The full url would be `BASE_URL/status` where the base url can be obtained from [here](https://docs.wayscript.com/platform/lairs/endpoints#viewing-your-lairs-endpoints).

You can also run the `example.py` by typing `python example.py` inside a WayScript terminal or press the play button in the top right corner of wayscript with `example.py` open.

# Run tests

You can run tests that cover the functionality by running

```
python -m pytest
```

# Further reading

[Setup a Flask Server (Python)](https://docs.wayscript.com/quickstart-spin-up-server/python/host-a-flask-server)
