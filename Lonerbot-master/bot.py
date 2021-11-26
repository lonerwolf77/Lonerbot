#smh no bad words in my bot.py file
import discord
import time
import random
import sys
import os
import json
from datetime import date
import datetime 
import time
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
    
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing,
        name=f"Default prefix: *"))
        
    #As you see here this line of code does cool things

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

    global StartTime
    StartTime = time.time()

@bot.event
async def on_guild_join(guild):
    with open('Cogs/Json/Servers.json', 'r') as f:
        prefixes = json.load(f)                                     

    prefixes[(guild.id)] = "*"

    with open('Cogs/Json/Servers.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.event 
async def on_guild_remove(guild):
    with open('Cogs/Json/Servers.json', 'r') as f:
        prefixes = json.load(f)
    
    prefixes.pop((guild.id))

    with open('Cogs/Json/Servers.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    #<-----------BOT COMMANDS---------->#





@bot.event
async def on_message(message):
    message.content = message.content.lower()
    await bot.process_commands(message)


@bot.command()
async def list(ctx):
    guilds = bot.guilds

    server_embed=discord.Embed(title="LonerBot is in " + str(len(bot.guilds)) + " servers", color=0x00fbff)

    for guild in guilds:
        server_embed.add_field(name="Name: " + str(guild.name), value="Members: " + str(guild.member_count), inline=False)

    await ctx.send(embed=server_embed)


@bot.event
async def on_guild_join(ctx):
    guild = bot.get_guild(id)
   
    print("Bot joined" + '')





@bot.command(pass_context=True)
async def logout(ctx):

    if ctx.author.id == 358617608377073665:
        await ctx.send("**Loging off**")
        await bot.logout()

    
    else:
        await ctx.send("```Command logout is not found```")

@bot.command()
async def status(ctx):
    bot.ping = round(bot.latency, 3)

    if bot.ping == 0:
        bot_status = 'huh???'
        color = 0

    elif bot.ping < 0.5:
        bot_status = ' :green_square:'
        color = 0x2ecc71

    elif bot.ping < 1.5:
        bot_status = ' :yellow_square:' 
        color = 0xf1c40f

    else:
        bot_status = ' :red_square:'
        color = 0xe74c3c


    embed=discord.Embed(title=str(bot.user.name) + ' Status', color=color)
    embed.set_thumbnail(url=bot.user.avatar_url)

    embed.add_field(name="Ping: ", value=str(bot.ping) + " " +bot_status, inline=False)

    uptime = str(datetime.timedelta(seconds=int(round(time.time()- StartTime))))
    embed.add_field(name="Uptime: ", value=str(uptime), inline=False)

    embed.add_field(name="Version: ", value=discord.__version__, inline=False) 

    await ctx.send(embed=embed)






bot.run(token)