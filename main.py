import discord
import logging
import asyncio
import json
from discord.ext import commands

bot = commands.Bot(command_prefix='.')  

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

with open('config.json', 'r') as json_data:
    config = json.load(json_data)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------------------')

@bot.command(pass_context=True)
async def say(ctx, *args):
    await bot.say(args)

        
    

client.run(config['token'])
