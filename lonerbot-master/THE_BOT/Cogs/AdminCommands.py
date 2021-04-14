import discord
from discord.ext import commands
import time
import random

class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def promote(self, ctx, *, user: discord.User):
            await user.create_dm()
            await user.dm_channel.send("noice")


    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def admin_help(self, ctx):
        ad_embed=discord.Embed(title="Admin Help", color=0xff0800)
        ad_embed.add_field(name="---ADMIN COMMANDS---", value="--------")
        ad_embed.add_field(name="/echo", value="repeats your message", inline=False)
        ad_embed.add_field(name="/kick", value="You must @ a member to kick them", inline=False)
        ad_embed.add_field(name="/ban", value="You must @ a member to ban them", inline=False)
        await ctx.send(embed=ad_embed)

        channel = self.bot.get_channel(829978424126210079)
        await channel.send(f"{ctx.author.name} has used command admin_help")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def echo(self, ctx, *, message=None):

        message = message
        await ctx.message.delete()
        await ctx.send(message)

        channel = self.bot.get_channel(829978424126210079)
        await channel.send(f"{ctx.author.name} has used command echo")


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def logout(self, ctx):
        await ctx.send('Shutting down')
        await self.logout()

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason = None):

        if reason == None:
            reason = "You may have done something wrong idk"

        if member == None:
            await ctx.send("You need to @ someone")
            return

        await member.ban(reason = reason)
        await ctx.send(str(member.mention) + " has been banned")

        print(f"{ctx.author.id}/{ctx.author.name} has used command ban")

        channel = self.bot.get_channel(829978424126210079)
        await channel.send(f"{ctx.author.name} has used command admin_help")



    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member = None):

        await member.kick()
        await ctx.send(str(member.mention) + " has been kicked")

        print(f"{ctx.author.id}/{ctx.author.name} has used command kick")

        channel = self.bot.get_channel(829978424126210079)
        await channel.send(f"{ctx.author.name} has used command kick")

        





def setup(bot):

    bot.add_cog(AdminCommands(bot))
