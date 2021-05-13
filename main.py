import discord
import os
from dotenv import load_dotenv
import requests
import json
load_dotenv()

client = discord.Client()
# SECRET_KEY = os.environ.get("ODQyMjYxODgxOTkyMzgwNDE3.YJyvgQ.GESdQVmhAXqex4x3xbcwC664HcU")
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$bussin'):
        await message.channel.send('Sheeeeesh')

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

client.run(os.getenv('TOKEN'))