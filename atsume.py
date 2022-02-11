import discord
import os, random
import borgor

from discord.ext import commands
from objects import config

bot = commands.Bot(command_prefix=config.prefix)

@bot.event
async def on_ready():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'Loaded {filename}')
        else:
            print(f'Unable to load {filename}')

    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    print(f'Connected! Running on {bot.user}')
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="you :3"))

bot.run(config.token)
