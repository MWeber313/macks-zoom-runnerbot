import os
import jwt
import requests
import json
import time
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

def generateToken():
	encoded = jwt.encode({'iss': API_KEY, 'exp': time.time() + 5000}, API_SECRET, algorithm="HS256")
	return encoded

meetingdetails = {
    "topic": "Dennyzens Hangout",
    "duration": "120",
    "timezone": "America/Los_Angeles",
    "agenda": "Study and hunt for jobs together",
    "type": 1,
    "settings": {
        "host_video": "false",
        "waiting_room": "false",
        "participant_video": "false",
        "join_before_host": "true",
        "mute_upon_entry": "false",
        "watermark": "true",
        "audio": "voip",
        "auto_recording": "none"
    }
}

def createMeeting():
    headers = {'authorization': 'Bearer ' + generateToken(), 'content-type': 'application/json'}
    response = requests.post(f'https://api.zoom.us/v2/users/me/meetings', headers=headers, data=json.dumps(meetingdetails))
    solution = json.loads(response.text) 
    join_URL = solution["join_url"] 
    join_URL = str(join_URL)
    return join_URL
