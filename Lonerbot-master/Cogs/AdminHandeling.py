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
        ad_embed.add_field(name="clear", value="Add the amount after a space(default amount 50)", inline=False)
        ad_embed.add_field(name="change_prefix", value="Changes the current prefix", inline=False)
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
        await channel.send(f"{ctx.author.name} has used command echo (the message was {message})")


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

        print(f"{ctx.author.id}/{ctx.author.name} has used command ban (person being banned {member.id}/{member.name}. from the server {ctx.message.guild.name})")

        channel = self.bot.get_channel(829978424126210079)
        await channel.send(f"{ctx.author.name} has used command ban (person being banned {member.id}/{member.name}. from the server {ctx.message.guild.name})")

        with open("l1.txt", 'a') as myfile:
            myfile.write(f'{ctx.author.name} has used command ban (person being banned {member.id}/{member.name}. from the server {ctx.message.guild.name})')

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member = None):

        if member == None:
            await ctx.send("You need to @ someone")
            return

        await member.kick()
        embed=discord.Embed(title=f":white_check_mark: " + str(member.name) +  " has been kicked", color=0xe74c3c)

        await ctx.send(embed=embed)

        print(f"{ctx.author.id}/{ctx.author.name} has used command kick (person being kicked {member.id}/{member.name}. from the server {ctx.message.guild.name})")

        channel = self.bot.get_channel(829978424126210079)
        await channel.send(f"{ctx.author.name} has used command kick (person being kicked {member.id}/{member.name}. from the server {ctx.message.guild.name})")

        with open("l1.txt", 'a') as myfile:
            myfile.write(f'{ctx.author.name} has used command kick (person being kicked {member.id}/{member.name}. from the server {ctx.message.guild.name})')

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, ammount=50):
        await ctx.channel.purge(limit=ammount)

        print(f"{ctx.author.id}/{ctx.author.name} has used command clear (ammount {ammount})") 

        channel = self.bot.get_channel(829978424126210079)
        await channel.send(f"{ctx.author.name} has used command clear (ammount {ammount})")

        with open("l1.txt", 'a') as myfile:
            myfile.write(f'{ctx.author.name} has used command clear (ammount {ammount}')

def setup(bot):

    bot.add_cog(AdminCommands(bot))