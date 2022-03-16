
import discord
from discord.ext import commands
import json

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
            print("Logged in as: " + str(self.bot.user.name) + " : " + str(self.bot.user.id) + "\n"
            "\n------------------------------")
            print("Running on discord version: " + discord.__version__)
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing,
            name=f"Default prefix: *"))

def setup(bot):
    bot.add_cog(Events(bot))
    
