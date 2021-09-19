#smh no bad words in my bot.py file
import discord
import time
import random
import sys
import os
import json
from datetime import date

from discord.ext import commands
from sys import platform as _platform, prefix



NULL = None

async def get_prefix(bot, message):
    with open('Cogs/Json/Servers.json', 'r') as f:
        prefixes = json.load(f) 
    
        #If the server ID is not in Server.json add it
        if str(message.guild.id) not in prefixes:
            prefixes[str(message.guild.id)] = "*"
            with open('Cogs/Json/Servers.json', 'w') as f:
                json.dump(prefixes, f, indent=4)

    return prefixes[str(message.guild.id)]


bot = commands.Bot(
    command_prefix=(get_prefix)
)



token = open("token.txt", "r").readline()

if token == None:
    print("Failed to find token.")

    time.sleep(1)


bot.remove_command('help')



#<--------CLEAR CONSOLE--------->#

if _platform == "linux" or _platform == "linux2":
    #Linux
    os.system('clear')

elif _platform == "win32" or "win64":
    #Windows
    os.system('cls')

    #<-----------BOT EVENTS---------->#



today = date.today()

@bot.event
async def on_ready():
    os.system('cls')
    print("Logged in as: " + str(bot.user.name) + " : " + str(bot.user.id) + "\n"
    "\n------------------------------")
    print("Running on discord version: " + discord.__version__, "Today's date:", today)

    with open("l1.txt", 'a') as myfile:
        myfile.write(f' {today}, ')

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing,
        name=f"Default prefix: *"))

    #<-----------LOAD COGS---------->#

    initial_extensions = ["Cogs.ErrorHandeling", "Cogs.AdminHandeling", "Cogs.Customization", "Cogs.Commands"]

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

@bot.event
async def on_guild_join(guild):
    with open('Cogs/Json/Servers.json', 'r') as f:
        prefixes = json.load(f)                                     

    prefixes[str(guild.id)] = "*"

    with open('Cogs/Json/Servers.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.event 
async def on_guild_remove(guild):
    with open('Cogs/Json/Servers.json', 'r') as f:
        prefixes = json.load(f)
    
    prefixes.pop(str(guild.id))

    with open('Cogs/Json/Servers.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    #<-----------BOT COMMANDS---------->#

@bot.command()
async def ping(ctx):
    ping = round(bot.latency, 3)
    await ctx.send(f"Ping: " + str(ping))

@bot.command()
async def invite(ctx):
    link = await ctx.channel.create_invite()
    await ctx.send("Here is your invite " + str(link))

    with open("l1.txt", 'a') as myfile:
        myfile.write(f"{ctx.author.name} has used command invite")

@bot.command()
async def bot_invite(ctx):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=720591908963090443&permissions=8&scope=bot")

@bot.command()
async def list(ctx):
    guilds = bot.guilds

    server_embed=discord.Embed(title="LonerBot is in " + str(len(bot.guilds)) + " servers", color=0x00fbff)

    for guild in guilds:
        server_embed.add_field(name="Name: " + str(guild.name), value="Members: " + str(guild.member_count), inline=False)

    await ctx.send(embed=server_embed)

@bot.command(pass_context=True)
async def logout(ctx):

    if ctx.author.id == 358617608377073665:
        await ctx.send("**Loging off**")
        await bot.logout()

    
    else:
        await ctx.send("Nice try ;)")

bot.run(token)