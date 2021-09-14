import sys
import discord
import json

from discord.ext import commands

class Customization(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
                
    @commands.command(pass_context=True)
    async def change_prefix(self, ctx, prefix):
        with open('Cogs/Json/Servers.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix
        
        with open('Cogs/Json/Servers.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

        await ctx.send("**Prefix Changed To:** " + prefix)

def setup(bot):
    bot.add_cog(Customization(bot))