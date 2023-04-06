import os
import discord
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

async def on_message(message):
    if message.author== client.user:
        return
    
    if message.content == '!zoom':
        

client.run(TOKEN)