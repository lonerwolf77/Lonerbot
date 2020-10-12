import discord
from discord.ext import commands

import random

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def help(self, ctx):                        
        embed=discord.Embed(title="Help", color=0x00fbff)
        embed.add_field(name="/help", value="sends this message", inline=False)
        embed.add_field(name="/invite", value="send an invite to the server", inline=False)
        embed.add_field(name="/echo", value="repeats your message")
        embed.add_field(name="/Random", value="Gives random number from 1-10", inline=False)
        embed.add_field(name="/Admin_help", value="Has all of the admin commands listed", inline=False)

        await ctx.send(embed=embed)


    @commands.command()
    async def random(self, ctx):
        number = random.randint(1, 10)
        await ctx.send(number)


    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"{member.name} joined")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"{member.name} left")

    @commands.command()
    async def rules(self, ctx):
        ad_embed=discord.Embed(title="Rules", color=0x00fbff)
        ad_embed.add_field(name="---RULES---", value="--------")
        ad_embed.add_field(name="Rule 1", value="No spamming", inline=False)
        ad_embed.add_field(name="Rule 2", value=" If you want to write sweardwords go to NSFW chat")
        await ctx.send(embed=ad_embed)


def setup(bot):

    bot.add_cog(Commands(bot))
