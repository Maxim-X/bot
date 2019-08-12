import discord
from discord.ext import commands
from discord.ext.commands import Bot

Bot = commands.Bot(command_prefix='!')

@Bot.event
async def on_ready():
	print('Бот онлайн!')

@Bot.command(pass_context = True)
async def hello():
	print('Бот онлайн!')

Bot.run("NTcxMzUzNDI3NzI1MjU0NjU3.XVGymg.GUTX95hrxDfOMRDDa1Un9NLKCUw")
