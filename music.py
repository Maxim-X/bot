import discord
from discord.ext import commands
from discord.ext.commands import Bot

Bot = commands.Bot(command_prefix='!')

@Bot.event
async def on_ready():
	print('Бот онлайн!')

@Bot.command(pass_context = True)
async def hello(ctx):
	await Bot.say("Hello!!!")

Bot.run("NjEwNTYyMjk2NjQ0ODk0NzIz.XVHIQA.h6hbS6mVsCdnJdf1YF7uRSVEHaA")
