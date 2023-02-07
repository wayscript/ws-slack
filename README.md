![img](https://i.ibb.co/Vgv9nf1/interface3.png)

# Spin Up a Slack Microservice using Flask

This template is an example of a web server inside the WayScript X lair environment that can query the Slack API. It includes 3 endpoints -

- `GET /channels` - get all the channels in a workspace
- `POST /message` send message to a channel or user
- `GET /status` checks whether the API is properly integrated with slack

## Requirements

Inside of your requirements.txt, it is required to include the dependencies of your project. In this example, we have `flask` and the slack sdk.

```python
flask
slack_sdk
```

## Setup

### 1) Setup a Slack App

In order to setup a slack app, complete the following tutorials.

- [Create an app](https://api.slack.com/authentication/basics#creating)
- [Request scopes](https://api.slack.com/authentication/basics#scopes) - Scopes dictate how much power your slack app posessess. For this tutorial, add the following scopes add the following scopes `channels:read`, `chat:write`, `chat:write.public`.
- [Install to a workspace of your choice](https://api.slack.com/authentication/basics#installing)

### 2) Setting up Flask

Flask Applications within WayScript X require three criteria:

- App.py file
- requirements.txt file
- Deploy trigger in .triggers file

#### App.py

The app.py file houses the flask application. This is where you can create routes, or url endpoints, and what response is given to the user when those routes are visited. Here is an example route:

```python
@app.route('/channels')
def response():
    channels = get_channels()
    return channels
```

In this specific example, the url will be the base url + '/channels'.

This will return a JSON response which is provided in the return statement.

#### Deploy Trigger

A deploy trigger allows easy, seamless deployments of your flask application. Add a deployment trigger to your .triggers file.
You are able to run your flask application with the following command placed in the command to run blank:

```python
flask run --port 8080 --host 0.0.0.0
```

The flask run command looks for the App.py file by default. This command will need to be modified if your flask application is placed in a file not called App.py

For the port blank you will need to place the same port number that is included in your flask run command. In this example that is

```python
8080
```

#### WayScript Lair Tools

A WayScript Lair allows you to have two separate environment of your flask application, a development environment and a production environment. Once you are finished developing your application, you can deploy to a separate, production state environment by using the deploy button on the left.

You can continue to to develop inside the development lair, then redeploy to your production state to reflect those changes in your production state application.

### 3) Save auth token to Lair

Go back to your newly created slack app's [settings page](https://api.slack.com/apps). Open the OAuth & Permissions section from the app sidebar. It's the same place you setup the app scopes. Copy the `Bot User OAuth Token`.

Next, save the key to the [`.secrets`](https://docs.wayscript.com/platform/lairs/environment-variables#example-.env-and-.secrets-files) file in your Lair. Set the `key` as `SLACK_API_TOKEN` and the `value` as the token you obtained from slack.

### 4) Verify that service is up and working correctly

Visit the `/status` endpoint. If you get "Slack API is connected and working properly", it means the service is running and authenticated to connect with your slack workspace. The full url would be `BASE_URL/status` where the base url can be obtained from [here](https://docs.wayscript.com/platform/lairs/endpoints#viewing-your-lairs-endpoints).
