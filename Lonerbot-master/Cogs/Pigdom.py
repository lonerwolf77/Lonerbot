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
        embed.add_field(name="Server", value="Get server-related info", inline=False)

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



    #@commands.command()
    #async def gen(self, ctx):
        #try:
            #r = requests.get("http://api.minehut.com/server/PigdomGN?byName=true")
            #json_data = r.json()
            #description = json_data["server"]["motd"]
            #online = str(json_data["server"]["online"])
            #playerCount = str(json_data["server"]["playerCount"])
            #maxPlayers = str(json_data["server"]["maxPlayers"])
            #platform = json_data["server"]["platform"]    

        #except Exception as e:
            #await ctx.send("Failed to find server.")
            #await ctx.send("\nError: " + str(e))
            #print("Failed to find server: " + str(e))
            #return 


        #embed = discord.Embed(
            #title="PigdomSMP" + " info",
            #description="Description: " + description + "\nonline: " + online + "\nPlayers: " + playerCount + "\nmaxPlayers: " + maxPlayers + "\nplatform: " + platform,
        
            #color=discord.Color.dark_green()
        #)
        #embed.set_thumbnail(url="https://cdn.discordapp.com/icons/817046907519500328/5db8b56a99513420b2825d07868bce57.webp?size=1024")


    @commands.command()
    async def apply (self, ctx):
        embed=discord.Embed(title="Apply", color=0x00fbff)
        embed.add_field(name="Apply for mod:", value="https://forms.gle/sqMwMSJeeZLM7H1E9", inline=False)
        embed.add_field(name="Apply for helper:", value="Currently unable to apply")

        await ctx.send(embed=embed)


    @commands.command() 
    async def meta(self, ctx):
        await ctx.send('Join the meta server: https://discord.gg/vuXVfKN93s')

def setup(bot):

    bot.add_cog(Pigdom(bot))