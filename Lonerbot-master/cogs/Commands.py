import discord
from discord.ext import commands
import os
import requests
import json
import time
import datetime





class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        global StartTime
        StartTime = time.time()

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
    async def link(self, ctx):
        await ctx.send("https://discord.com/api/oauth2/authorize?client_id=720591908963090443&permissions=8&scope=bot")

    @commands.command()
    async def status(self, ctx):
        self.bot.ping = round(self.bot.latency, 3)

        if self.bot.ping == 0:
            bot_status = 'huh???'
            color = 0

        elif self.bot.ping < 0.5:
            bot_status = ' :green_square:'
            color = 0x2ecc71

        elif self.bot.ping < 1.5:
            bot_status = ' :yellow_square:' 
            color = 0xf1c40f

        else:
            bot_status = ' :red_square:'
            color = 0xe74c3c


        embed=discord.Embed(title=str(self.bot.user.name) + ' Status', color=color)
        embed.set_thumbnail(url=self.bot.user.avatar_url)

        embed.add_field(name="Ping: ", value=str(self.bot.ping) + " " +bot_status, inline=False)

        uptime = str(datetime.timedelta(seconds=int(round(time.time()- StartTime))))
        embed.add_field(name="Uptime: ", value=str(uptime), inline=False)

        embed.add_field(name="Version: ", value=discord.__version__, inline=False) 

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
        embed.add_field(name="Smp", value="Get PigdomSMP-related info", inline=False)
        embed.add_field(name="Gen", value="Get PigdomGN-related info(Work in proggress)", inline=False)
        embed.add_field(name="Life", value="Get PigdomLife-related info", inline=False)

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
    async def life(self, ctx):
        try:
            r = requests.get("http://api.minehut.com/server/pigdomlife?byName=true")
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
            title="PigdomLife" + " info",
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

    bot.add_cog(Commands(bot))
