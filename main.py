import discord
import os
from dotenv import load_dotenv
load_dotenv()

client = discord.Client()
# SECRET_KEY = os.environ.get("ODQyMjYxODgxOTkyMzgwNDE3.YJyvgQ.GESdQVmhAXqex4x3xbcwC664HcU")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))