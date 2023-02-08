# Sample app to test the Slack microservice
import json
import os
import requests
from wayscript.utils import get_application_key

WAYSCRIPT_LAIR_URL = os.getenv('WAYSCRIPT_LAIR_URL')
session = requests.Session()
session.headers["authorization"] = f"Bearer {get_application_key()}"


status_resp = session.get(f'{WAYSCRIPT_LAIR_URL}/status')
print(status_resp.text)

channels_resp = session.get(f'{WAYSCRIPT_LAIR_URL}/channels')
channels = json.loads(channels_resp.text)

print(f"The message will be sent to {channels[0][1]}. Proceed (Y/n)?")
choice = input()
if choice == "Y":
    data = {
        "target_id": channels[0][0],
        "message": "Hello :tada:"
    }

    message_post_resp = session.post(f"{WAYSCRIPT_LAIR_URL}/message", json=data)
    print(message_post_resp.text)
else:
    print("Message not sent")
