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
            embed.add_field(name="coinflip", value="Flip a coin get heads or tails", inline=False)
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
            embed.add_field(name="coinflip", value="Flip a coin get heads or tails", inline=False)
            embed.add_field(name="status", value="Gives information on the bots status", inline=False)
            embed.add_field(name="tag", value="Get pigdom exlusive commands", inline=False)


            await ctx.send(embed=embed)

    @commands.command()
    async def support(self, ctx):
        await ctx.send('Get support at <#869581433885323275>')


    @commands.command()
    async def tag(self, ctx):
        embed=discord.Embed(title="PigdomSMP-exclusive commands", color=0)
        embed.add_field(name="support", value="Instructions for community support", inline=False)
        embed.add_field(name="apply", value="Apply here")
        embed.add_field(name="meta", value="Join the meta discord", inline=False)
        embed.add_field(name="Server", value="Get server-related info", inline=False)

        await ctx.send(embed=embed)
        

    @commands.command()
    async def boost(self, ctx):
        embed=discord.Embed(title="Boost the discord server!")
        embed.add_field(name="Access to #boosters", value="a private text channel for boosters")
        embed.add_field(name="Access to #boost-cmds", value="a secret command channel")
        embed.add_field(name="Access to #memes", value="a private memes channel")
        embed.add_field(name="Last but not least", value="you also get a vc")

        await ctx.send(embed=embed)


    @commands.command()
    async def random(self, ctx):
        number = random.randint(1, 10)
        await ctx.send(number)


    @commands.command()
    async def server(self, ctx):
        try:
            r = requests.get("http://api.minehut.com/server/PigdomSMP?byName=true")
            json_data = r.json()
            description = json_data["server"]["motd"]
            online = str(json_data["server"]["online"])
            playerCount = str(json_data["server"]["playerCount"])
            maxPlayers = str(json_data["server"]["maxPlayers"])
            platform = json_data["server"]["platform"]    

        except Exception as e:
            await ctx.send("Failed to find server.")
            await ctx.send("\nError: " + str(e))
            print("Failed to find server: " + str(e))
            return 


        embed = discord.Embed(
            title="PigdomSMP" + " info",
            description="Description: " + description + "\nonline: " + online + "\nPlayers: " + playerCount + "\nmaxPlayers: " + maxPlayers + "\nplatform: " + platform,
        
            color=discord.Color.dark_green()
        )
        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/817046907519500328/5db8b56a99513420b2825d07868bce57.webp?size=1024")

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

        

    @commands.command(aliases=['flip', 'coin'])
    async def coinflip(self, ctx):
        coinsides = ['Heads', 'Tails']
        await ctx.send(f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinsides)}**!")
    
    @commands.command()
    async def apply (self, ctx):
        embed=discord.Embed(title="Apply", color=0x00fbff)
        embed.add_field(name="Apply for mod:", value="https://forms.gle/sqMwMSJeeZLM7H1E9", inline=False)
        embed.add_field(name="Apply for helper:", value="Currently unable to apply")

        await ctx.send(embed=embed)
        


    @commands.command() 
    async def meta(self, ctx):
        await ctx.send('Join the meta server: https://discord.gg/vuXVfKN93s')

    @commands.command()
    async def invite(self, ctx):
        link = await ctx.channel.create_invite()
        await ctx.send("Here is your invite " + str(link))



        
def setup(bot):

    bot.add_cog(Commands(bot))
