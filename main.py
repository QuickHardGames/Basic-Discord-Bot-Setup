#Join My Discord Server - https://discord.gg/rptymubqW5
#Go to My Website for More Codes!!

#Imports
import discord
from discord.ext import commands

#Prefix

client = commands.Bot(command_prefix="?")


#Basic Command
@client.command()
async def hi(ctx):
  await ctx.send("Hello!")
  
#Running The Bot
client.run("ENTER YOUR TOKEN HERE")
