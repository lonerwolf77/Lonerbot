import discord
from discord.ext import commands
import subprocess

import random

import os
import requests


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        
    

    @commands.command()
    async def help(self, ctx):
        if ctx.message.author.guild_permissions.manage_messages:
            embed=discord.Embed(title="Help", color=0x546e7a)
            embed.add_field(name="help", value="Sends this message", inline=False)
            embed.add_field(name="invite", value="Send an invite to the server")
            embed.add_field(name="Random", value="Gives random number from 1-10", inline=False)
            embed.add_field(name="status", value="Gives information on the bots status", inline=False)
            embed.add_field(name="tag", value="Get pigdom exlusive commands", inline=False)

            await ctx.send(embed=embed)


            embed=discord.Embed(title="---------------------", color=0xff0800)
            embed.add_field(name="admin_help", value="Gives list of admin comands", inline=True)

            await ctx.send(embed=embed)



        else:
            embed=discord.Embed(title="Help", color=0x546e7a)
            embed.add_field(name="help", value="Sends this message", inline=False)
            embed.add_field(name="invite", value="Send an invite to the server")
            embed.add_field(name="random", value="Gives random number from 1-10", inline=False)
            embed.add_field(name="status", value="Gives information on the bots status", inline=False)
            embed.add_field(name="tag", value="Get pigdom exlusive commands", inline=False)


            await ctx.send(embed=embed)

    @commands.command()
    async def minecraft(self, ctx, arg):
        try:
            r = requests.get("http://api.minehut.com/server/"+ arg +"?byName=true")
            json_data = r.json()
            print(json_data)
            description = json_data["server"]["motd"]
            online = str(json_data["server"]["online"])
            playerCount = str(json_data["server"]["playerCount"])
            maxPlayers = str(json_data["server"]["maxPlayers"])
            platform = json_data["server"]["platform"]    

        except:
            await ctx.send("Failed to find server.")
            print("Failed to find a server")
            return 


        embed = discord.Embed(
            title=arg + " info",
            description="Description: " + description + "\nonline: " + online + "\nPlayers: " + playerCount + "\nmaxPlayers: " + maxPlayers + "\nplatform: " + platform,

            color=discord.Color.dark_green()
        )
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/minecraft_gamepedia/images/9/93/Grass_Block_JE7_BE6.png/revision/latest?cb=20200830143209")

        await ctx.send(embed=embed)
        


    
        
    @commands.command()
    async def data(self, ctx):
        embed = discord.Embed(title="Server Data", color=0xFF5733)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name="Server Name", value=ctx.message.guild.name, inline=False)
        embed.add_field(name="Server was created on", value=ctx.guild.created_at.strftime("%b %d, %Y"), inline=False)
        embed.add_field(name="Number Of Members", value=ctx.guild.member_count, inline=False)
        embed.add_field(name="Number Of Roles", value=len(ctx.guild.roles), inline=True)
    

        text_channel_list = []
        for channel in ctx.guild.text_channels:
            text_channel_list.append(channel)

        voice_channel_list = []
        for channel in ctx.guild.voice_channels:
            voice_channel_list.append(channel)

        embed.add_field(name="Number Of Text Channels", value=len(text_channel_list), inline=False)
        embed.add_field(name="Number Of Voice Channels", value=len(voice_channel_list), inline=False)
        await ctx.send(embed=embed)


    @commands.command()
    async def invite(self, ctx):
        link = await ctx.channel.create_invite()
        await ctx.send("Here is your invite " + str(link))

    @commands.command()
    async def report(self, ctx, *, message=None):

        message = message
        await ctx.message.delete()
        
        
        
        embed=discord.Embed(title=f"***{ctx.author.name} has filed a report: ***" + ' ' + f"{message}" , color=0xe74c3c)

        channel = self.bot.get_channel(942034077010231336)
        await channel.send(embed=embed)

    @commands.command()
    async def list(self, ctx):
        guilds = self.bot.guilds

        server_embed=discord.Embed(title="LonerBot is in " + str(len(self.bot.guilds)) + " servers", color=0x00fbff)

        for guild in guilds:
            server_embed.add_field(name="Name: " + str(guild.name), value="Members: " + str(guild.member_count), inline=False)

        await ctx.send(embed=server_embed)


    @commands.command(pass_context=True)
    async def logout(self, ctx):

        if ctx.author.id == 358617608377073665:
            await ctx.send("**Loging off**")
            await self.bot.logout()

    
        else:
            await ctx.send("```Command logout is not found```")



    @commands.command()
    async def bot_invite(self, ctx):
        await ctx.send("https://discord.com/api/oauth2/authorize?client_id=720591908963090443&permissions=8&scope=bot")


        
def setup(bot):

    bot.add_cog(Commands(bot))
