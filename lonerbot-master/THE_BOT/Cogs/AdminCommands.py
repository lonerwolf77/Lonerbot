import discord
from discord.ext import commands

class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def promote(self, ctx, *, user: discord.User):
            await user.create_dm()
            await user.dm_channel.send("noice")

            print("Message send")


    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def admin_help(self, ctx):
        ad_embed=discord.Embed(title="Admin Help", color=0xff0800)
        ad_embed.add_field(name="---MEMBER COMMANDS---", value="--------")
        ad_embed.add_field(name="/help", value="sends this message", inline=False)
        ad_embed.add_field(name="/invite", value="send an invite to the server", inline=False)
        ad_embed.add_field(name="---ADMIN COMMANDS---", value="--------")
        ad_embed.add_field(name="/echo", value="repeats your message", inline=False)
        ad_embed.add_field(name="/promote", value="#UNDER CONSTRUCTION#", inline=False)
        await ctx.send(embed=ad_embed)


    @commands.command()
    async def offline():
        self.logout()


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def echo(self, ctx, *, message=None):

        message = message
        await ctx.message.delete()
        await ctx.send(message)



def setup(bot):

    bot.add_cog(AdminCommands(bot))
