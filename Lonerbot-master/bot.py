#smh no bad words in my bot.py file
import discord
import time
import random
import sys
import os
import json
from datetime import date
from discord.utils import get


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
    

class colors:
    default = 0
    teal = 0x1abc9c
    dark_teal = 0x11806a
    green = 0x2ecc71
    dark_green = 0x1f8b4c
    blue = 0x3498db
    dark_blue = 0x206694
    purple = 0x9b59b6
    dark_purple = 0x71368a
    magenta = 0xe91e63
    dark_magenta = 0xad1457
    gold = 0xf1c40f
    dark_gold = 0xc27c0e
    orange = 0xe67e22
    dark_orange = 0xa84300
    red = 0xe74c3c
    dark_red = 0x992d22
    lighter_grey = 0x95a5a6
    dark_grey = 0x607d8b
    light_grey = 0x979c9f
    darker_grey = 0x546e7a
    blurple = 0x7289da
    greyple = 0x99aab5




@bot.command()
async def invite(ctx):
    link = await ctx.channel.create_invite()
    await ctx.send("Here is your invite " + str(link))

    

@bot.command()
async def bot_invite(ctx):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=720591908963090443&permissions=8&scope=bot")


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

    gid = str(guild.id)
    print(f"{gid}")





@bot.command(pass_context=True)
async def logout(ctx):

    if ctx.author.id == 358617608377073665:
        await ctx.send("**Loging off**")
        await bot.logout()

    
    else:
        await ctx.send("```Command logout is not found```")




bot.run(token)