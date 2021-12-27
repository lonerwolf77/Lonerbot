import discord
from discord.ext import commands
import time
import random

class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def admin_help(self, ctx):
        ad_embed=discord.Embed(title="Admin Help", color=0xff0800)
        ad_embed.add_field(name="---ADMIN COMMANDS---", value="--------")
        ad_embed.add_field(name="echo", value="repeats your message", inline=False)
        ad_embed.add_field(name="kick", value="You must @ a member to kick them", inline=False)
        ad_embed.add_field(name="ban", value="You must @ a member to ban them", inline=False)
        ad_embed.add_field(name="purge", value="Add the amount after a space(default amount 50)")
        ad_embed.add_field(name="change_prefix", value="Changes the current prefix", inline=False)
        ad_embed.add_field(name="leave", value="Makes the bot leave the server", inline=False)
        ad_embed.add_field(name="lock", value="Lock a channel", inline=False)
        ad_embed.add_field(name="unlock", value="Unlock a channel", inline=False)
        
        await ctx.send(embed=ad_embed)

    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def lock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages = False)
        embed=discord.Embed(title=f":white_check_mark: " + "***Channel has been locked.***", color=0xe74c3c)

        await ctx.send(embed=embed)



    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def unlock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages = True)
        embed=discord.Embed(title=f":white_check_mark: " + "***Channel has been unlocked.***", color=0xe74c3c)

        await ctx.send(embed=embed)


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def echo(self, ctx, *, message=None):

        message = message
        await ctx.message.delete()
        await ctx.send(message)

        

    @commands.command(pass_context=True)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason = None):

        if reason == None:
            reason = "You may have done something wrong idk"

        if member == None:
            await ctx.send("You need to @ someone")
            return

        await member.ban(reason = reason)

        embed=discord.Embed(title=f":white_check_mark: " + str(member.name) +  " has been banned", color=0xe74c3c)

        await ctx.send(embed=embed)


        

    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None):

        if member == None:
            await ctx.send("You need to @ someone")
            return

        await member.kick()
        embed=discord.Embed(title=f":white_check_mark: " + str(member.name) +  " has been kicked", color=0xe74c3c)

        await ctx.send(embed=embed)

        

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, ammount=50):
        await ctx.channel.purge(limit=ammount)

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def leave(self, ctx):
        await ctx.guild.leave()


    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member=None):

        if member == None:
            await ctx.send("You need to @ someone")
            return

        #role = self.bot_get(ctx.guild.roles, name='Muted')

        role = self.bot.ctx.guild.roles(ctx.guild.roles, name='Muted')

        await member.add_roles(role)
        



def setup(bot):

    bot.add_cog(AdminCommands(bot))