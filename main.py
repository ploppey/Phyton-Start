import asyncio
from datetime import datetime

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

botcolor = 0x6A0888 #your Botcolor for Embeds

bot.remove_command('help')

########################################################################################################################
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print(discord.utils.oauth_url(bot.user.id))
    bot.loop.create_task(status_task())

########################################################################################################################
async def status_task():
    while True:
    # Setting `Playing ` status
    await bot.change_presence(activity=discord.Game(name="a game"))

    # Setting `Streaming ` status
    await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

    # Setting `Listening ` status
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

    # Setting `Watching ` status
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))

########################################################################################################################
@bot.command()
@commands.is_owner()
async def reboot(ctx):
    await ctx.channel.send("Rebooting!")
    await bot.logout()

########################################################################################################################
bot.run(TOKEN) #type in here your Token.
