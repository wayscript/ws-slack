# Sample app to test the Slack microservice
import requests

WAYSCRIPT_LAIR_URL = "<lair name>"

r = requests.get(f'{WAYSCRIPT_LAIR_URL}/status')
print(r.text)

r = requests.get(f'{WAYSCRIPT_LAIR_URL}/channels')
print(r.text)

data = {
    "target_id": "<target id obtained from previous /channels>",
    "message": "Hello :tada:"
}

r = requests.post(f"{WAYSCRIPT_LAIR_URL}/message", json=data)
print(r.text)
