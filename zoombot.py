import os
import discord
from discord.ext import commands
import jwt
import requests
import json
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

def generateToken():
	encoded = jwt.encode({'iss': API_KEY, 'exp': time() + 5000}, API_SECRET, algorithm="HS256")
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
    URL = print(f"{join_URL}")
    return join_URL












# START OF DISCORD CONTENT


TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
intents.members = True
intents.message_content = True
intents.typing = True
intents.prescences = True


bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content == 'test':
        await message.channel.send("Test!")
        return

# client = discord.Client(intents=intents)

# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')



# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
    
#     if message.content == '!test':
#         await message.channel.send("Test!")
#         return
    
#     if message.content == 'zoom!':
#         print('Hi')
#         response = createMeeting()
#         await message.channel.send(response)
#         return

bot.run(TOKEN)