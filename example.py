# Sample app to test the Slack microservice
import requests
import json
import os

WAYSCRIPT_LAIR_URL = os.getenv('WAYSCRIPT_LAIR_URL')

r = requests.get(f'{WAYSCRIPT_LAIR_URL}/status')
print(r.text)

r = requests.get(f'{WAYSCRIPT_LAIR_URL}/channels')
print(r.text)

channels = json.loads(r.text)
print(f"The message will be sent to {channels[0][1]}. Proceed (Y/n)?")
choice = input()
if choice == "Y":
    data = {
        "target_id": channels[0][0],
        "message": "Hello :tada:"
    }

    r = requests.post(f"{WAYSCRIPT_LAIR_URL}/message", json=data)
    print(r.text)
else:
    print("Message not sent")
