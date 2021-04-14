import discord
from discord.ext import commands
import requests



Bot = commands.Bot(command_prefix="!")


@Bot.event
async def on_ready():
    print("v1.0")
    print("Logged in as: " + str(Bot.user.name) + " : " + str(Bot.user.id) + "\n")
#R21301
@Bot.command()
async def Minecraft(ctx):
    r = requests.get(""+ arg +"?byName=true")
    json_data = r.json()
    print(json_data)
    description = json_data["Server"]

@bot.event 
async def on_ready():
    print("Cunt")

Bot.run("NzcxMDM2ODc5NDc3OTMyMDYy.X5mSDQ.yQByLJcXxpzFowv1sjKT9rWqEXU")