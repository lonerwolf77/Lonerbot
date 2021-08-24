import discord
from discord.ext import commands

import random

import requests

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def help(self, ctx):                        
        embed=discord.Embed(title="Help", color=0x00fbff)
        embed.add_field(name="/help", value="Sends this message", inline=False)
        embed.add_field(name="/invite", value="Send an invite to the server")
        embed.add_field(name="/Random", value="Gives random number from 1-10", inline=False)
        embed.add_field(name="/Admin_help", value="Has all of the admin commands listed", inline=False)
        embed.add_field(name="/coinflip", value="Flip a coin get heads or tails", inline=False)
        embed.add_field(name="/rolldice", value="Roll a dice get a number from 1 to 6", inline=False)
        embed.add_field(name="/ping", value="Used to test bot latency", inline=False)

        await ctx.send(embed=embed)

        print(f"{ctx.author.id}/{ctx.author.name} has used command help")

        channel = self.bot.get_channel(829978424126210079)
        await channel.send(f"{ctx.author.name} has used command help")


    @commands.command()
    async def random(self, ctx):
        number = random.randint(1, 10)
        await ctx.send(number)

        print(f"{ctx.author.id}/{ctx.author.name} has used command random")

        channel = self.bot.get_channel(829978424126210079)
        await channel.send(f"{ctx.author.name} has used command random")


    @commands.command()
    async def rules(self, ctx):
        ad_embed=discord.Embed(title="Rules", color=0x00fbff)
        ad_embed.add_field(name="---RULES---", value="------------------")
        ad_embed.add_field(name="Rule 1", value="e", inline=False)
        ad_embed.add_field(name="Rule 2", value="e")
        ad_embed.add_field(name="Rule 3 ", value="e", inline=False)
        ad_embed.add_field(name="Rule 4 ", value="e", inline=False)
        ad_embed.add_field(name="Rule 5", value="e", inline=False)
        ad_embed.add_field(name="Rule 6", value="e", inline=False)
        ad_embed.add_field(name="Rule 7", value="e", inline=False)
        ad_embed.add_field(name="Rule 8", value="e", inline=False)
        ad_embed.add_field(name="Rule 9", value="e", inline=False)
        ad_embed.add_field(name="Rule 10", value="e", inline=False)
        ad_embed.add_field(name="Rule 11", value="e", inline=False)

        await ctx.send(embed=ad_embed)

        print(f"{ctx.author.id}/{ctx.author.name} has used command rules")

        channel = self.bot.get_channel(829978424126210079)
        await channel.send(f"{ctx.author.name} has used command rules")

    @commands.command()
    async def the_rules(self, ctx):
        ad_embed=discord.Embed(title="M", color=0x00fbff)
        ad_embed.add_field(name="------", value="------------------")
        ad_embed.add_field(name="Rule 1", value="e", inline=False)
        ad_embed.add_field(name="Rule 2", value="e", inline=False)
        ad_embed.add_field(name="Rule 3", value="e") 
        ad_embed.add_field(name="Rule 4", value="e", inline=False)
        ad_embed.add_field(name="Rule 5", value="e", inline=False)

        await ctx.send(embed=ad_embed)

        print(f"{ctx.author.id}/{ctx.author.name} has used command the_rules")

        channel = self.bot.get_channel(829978424126210079)
        await channel.send(f"{ctx.author.name} has used command the_rules")

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

        

    @commands.command(aliases=['flip', 'coin'])
    async def coinflip(self, ctx):
        coinsides = ['Heads', 'Tails']
        await ctx.send(f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinsides)}**!")

        print(f"{ctx.author.id}/{ctx.author.name} has used command coinflip") 

        channel = self.bot.get_channel(829978424126210079)
        await channel.send(f"{ctx.author.name} has used command coinflip")

    @commands.command()
    async def rolldice(self, ctx):
        number = random.randint(1, 6)
        await ctx.send(F"You rolled a {number}")

        print(f"{ctx.author.id}/{ctx.author.name} has used command rolldice") 

        channel = self.bot.get_channel(829978424126210079) 
        await channel.send(f"{ctx.author.name} has used command rolldice")                  
  
    @commands.command()
    async def dyno(self, ctx):
        await ctx.send("https://discord.com/oauth2/authorize?client_id=161660517914509312&scope=bot%20identify%20guilds%20applications.commands&response_type=code&redirect_uri=https://dyno.gg/return&permissions=2134207679&state=o_7uOndog8udOeTHcZpjs")


def setup(bot):

    bot.add_cog(Commands(bot))