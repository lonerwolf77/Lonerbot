import discord
import json
import os

from utils import config

from discord.ext import commands


def main():
    intents = discord.Intents.default()
    intents.members = True

    global config
    config = config.config()

    bot = commands.Bot(
        intents=intents,
        command_prefix=config["prefix"]
    )

    

    
    os.system('cls')
    bot.remove_command('help')


    cogs = [
        "cogs.Events",
        "cogs.Commands",
        "cogs.ErrorHandeling",
        "cogs.AdminHandeling"
    ]

    for cog in cogs:
        bot.load_extension(cog)



    try:
        bot.run(config["token"])
    except Exception as e:
        print(f"Error when logging in: " + str(e))


if __name__ == "__main__":
    main()
