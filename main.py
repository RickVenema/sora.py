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


with open('config.json', 'r') as json_data:
    config = json.load(json_data)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------------------------')


@bot.command(pass_context=True)
async def say(ctx, arg):
    await bot.say(arg)


@bot.command(pass_context=True)
async def kick(ctx, member: discord.User):
    author = ctx.message.author
    test = author.permissions_in(ctx.message.channel)
    if test.kick_members== True:
        await bot.kick(member)
    else:
        await bot.say("NOPE")

bot.run(config['token'])
