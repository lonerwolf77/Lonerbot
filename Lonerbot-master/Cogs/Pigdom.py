import discord
from discord.ext import commands
import time
import json
import subprocess
import random
import os
import requests




class Pigdom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def support(self, ctx):
        await ctx.send('Get support at <#869581433885323275>')

    @commands.command()
    async def tag(self, ctx):
        embed=discord.Embed(title="PigdomSMP-exclusive commands", color=0)
        embed.add_field(name="support", value="Instructions for community support", inline=False)
        embed.add_field(name="apply", value="Apply here")
        embed.add_field(name="meta", value="Join the meta discord", inline=False)
        embed.add_field(name="smp", value="Get PigdomSMP-related info", inline=False)
        embed.add_field(name="gen", value="Get PigdomGN-related info(Work in proggress)", inline=False)

        await ctx.send(embed=embed)



    @commands.command()
    async def smp(self, ctx):
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
    async def gen(self, ctx):
        try:
            r = requests.get("http://api.minehut.com/server/pigdomgn?byName=true")
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
            title="Pigdomgn" + " info",
            description="Description: " + description + "\nonline: " + online + "\nPlayers: " + playerCount + "\nmaxPlayers: " + maxPlayers + "\nplatform: " + platform,
        
            color=discord.Color.dark_green()
        )
        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/817046907519500328/5db8b56a99513420b2825d07868bce57.webp?size=1024")


        await ctx.send(embed=embed)


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
    async def boost(self, ctx):
        embed=discord.Embed(title="Boost the discord server!")
        embed.add_field(name="Access to #boosters", value="a private text channel for boosters")
        embed.add_field(name="Access to #boost-cmds", value="a secret command channel")
        embed.add_field(name="Access to #memes", value="a private memes channel")
        embed.add_field(name="Last but not least", value="you also get a vc")

        await ctx.send(embed=embed)

def setup(bot):

    bot.add_cog(Pigdom(bot))