import discord
import random
import requests
import json
from Weather import*

TOKEN = #Enter Discord Bot Code in Here
api_key = #Enter API key for weather data here
command_prefix = 'w. '

client = discord.Client()


@client.event
async def on_ready():
    print('We are logged in as {0.user}'.format(client))

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{command_prefix}.[location]'))

@client.event
async def on_message(message):
    if message.author != client.user and message.content.startswith(command_prefix):
        location = message.content.replace(command_prefix, '').lower()
        if len(location) >= 1:
            url = f'' #Enter in the API URL link here
            try:
                data = json.loads(requests.get(url).content)
                data = parse_data(data)
                await message.channel.send(embed=weather_message(data, location))
            except KeyError:
                await message.channel.send(embed=error_message(location))

client.run(TOKEN)
