import discord
import time

import sys, traceback

from builtins import input

from discord.ext import commands
from discord.ext.commands import has_permissions

prefix = "/"

bot = commands.Bot(command_prefix=prefix, case_insensitive=True)

token = open("token.txt", "r").readline()

bot.remove_command('help')


base_cogs = ["Cogs.AdminCommands", "Cogs.ErrorHandeling", "Cogs.Commands"]


##LOAD COGS##

for extensions in base_cogs:
    bot.load_extension(extensions)

@bot.event
async def on_ready():
    print("v1.2")
    print("Logged in as: " + str(bot.user.name) + " : " + str(bot.user.id) + "\n"
    "My current prefix is: " + prefix + "\n------------------------------")
    await bot.change_presence(activity=discord.Game(name="/help"))

@bot.command()
async def invite(ctx):
    link = await ctx.channel.create_invite()
    await ctx.send("Here is your invite " + str(link))


### COGS ###
@bot.command()
async def load(ctx):
    try:
        bot.load_extension("Cogs.AdminCommands")
        bot.load_extension("Cogs.Comands")
        bot.load_extension("Cogs.ErrorHandeling")
        await ctx.send("Loaded cogs")
    except Exception as e:
        await ctx.send("Something went wrong while loading the cogs")
        print("Error: " + str(e))

@bot.command()
async def unload(ctx):
    try:
        bot.unload_extension("Cogs.AdminCommands")
        bot.unload_extension("Cogs.ErrorHandeling")
        bot.unload_extension("Cogs.Commands")
        await ctx.send("Unloaded cogs")
    except Exception as e:
        await ctx.send("Something went wrong when unloading the cogs")
        print("Error: " + str(e))


@bot.command()
async def reload(ctx):
    bot.unload_extension("Cogs.AdminCommands")
    bot.unload_extension("Cogs.ErrorHandeling")
    bot.unload_extension("Cogs.Commands")

    bot.load_extension("Cogs.AdminCommands")
    bot.load_extension("Cogs.ErrorHandeling")
    bot.load_extension("Cogs.Commands")

    await ctx.send("Reloaded all cogs")

###########



bot.run(token)
