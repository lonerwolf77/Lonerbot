import discord
from discord.ext import commands
import time
import random

class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
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
    async def data(self, ctx):
        embed = discord.Embed(title="Server Data", color=0xFF5733)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name="Server Name", value=ctx.message.guild.name, inline=False)
        embed.add_field(name="Amount Of Members", value=ctx.guild.member_count, inline=False)
        embed.add_field(name="Amount Of Roles", value=len(ctx.guild.roles), inline=True)

        text_channel_list = []
        for channel in ctx.guild.text_channels:
            text_channel_list.append(channel)

        voice_channel_list = []
        for channel in ctx.guild.voice_channels:
            voice_channel_list.append(channel)

        embed.add_field(name="Amount Of Text Channels", value=len(text_channel_list), inline=False)
        embed.add_field(name="Amount Of Voice Channels", value=len(voice_channel_list), inline=False)
        await ctx.send(embed=embed)




    @commands.command()
    @commands.has_permissions(administrator=True)
    async def echo(self, ctx, *, message=None):

        message = message
        await ctx.message.delete()
        await ctx.send(message)



        

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
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
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member = None):

        if member == None:
            await ctx.send("You need to @ someone")
            return

        await member.kick()
        embed=discord.Embed(title=f":white_check_mark: " + str(member.name) +  " has been kicked", color=0xe74c3c)

        await ctx.send(embed=embed)

        

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx, ammount=50):
        await ctx.channel.purge(limit=ammount)
        

        

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def leave(self, ctx):
        await ctx.guild.leave()

def setup(bot):

    bot.add_cog(AdminCommands(bot))