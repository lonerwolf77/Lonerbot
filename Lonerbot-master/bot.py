#i swear this bot is fucking braindead

import discord
import time
import random
import sys
import os

from discord.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned_or("*")
                ,case_insensative=True
                ,intents=discord.Intents().all())

token = open("token.txt", "r").readline()

if token == None:
    print("Failed to find token.")

    time.sleep(1)


bot.remove_command('help')

    #<-----------BOT EVENTS---------->#

os.system('cls')

@bot.event
async def on_ready():
    print("Logged in as: " + str(bot.user.name) + " : " + str(bot.user.id) + "\n"
    "My current prefix is: " + "*" + "\n------------------------------")
    print("Running on discord version: " + discord.__version__)

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing,
        name="OwO"))


    #<-----------LOAD COGS---------->#

    initial_extensions = ["Cogs.ErrorHandeling", "Cogs.AdminHandeling", "Cogs.Commands"]

    try:
        for extension in initial_extensions:
            bot.load_extension(extension)

        print("Loaded all cogs with 0 errors\n")

    except Exception as e:
        print("\nFailed to load cogs")
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)

    #<-----------BOT COMMANDS---------->#

@bot.command()
async def ping(ctx):
    ping = round(bot.latency, 3)
    await ctx.send(f"Ping: " + str(ping))

@bot.command()
async def invite(ctx):
    link = await ctx.channel.create_invite()
    await ctx.send("Here is your invite " + str(link))

    channel = bot.get_channel(829978424126210079)
    await channel.send(f"{ctx.author.name} has used command invite")

@bot.command()
async def bot_invite(ctx):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=720591908963090443&permissions=8&scope=bot")


@bot.event
async def on_guild_join(guild):

    guild.id = guild.id
    guild.name = guild.name

    Gjoin = (f"{bot.user.name} has joined {guild.id}/{guild.name}") 
    with open("l1.txt", 'a') as myfile:
        myfile.write(f'{Gjoin}, ')
        




bot.run(token)
