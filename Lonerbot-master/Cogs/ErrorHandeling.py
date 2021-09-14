import discord
from discord.ext import commands

class ErrorHandeling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return

        elif isinstance(error, commands.DisabledCommand):
            return await ctx.send(f'{ctx.command} has been disabled.')

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                return await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
            except:
                pass

        elif isinstance(error, commands.BadArgument):
             await ctx.send("```ERROR: Bad Argument!```")

        elif isinstance(error, commands.CommandNotFound):
            await ctx.send("```ERROR: Command not found!```")

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("```ERROR: Missing Permissions!```")

        elif isinstance(error, commands.CommandInvokeError):
             await ctx.send("```ERROR: Command Invoke Error!```")

        elif isinstance(error, commands.MissingRequiredArgument):
             await ctx.send("```ERROR: Missing Required Argument!```")

        else:
            await ctx.send("```Unkown Error!```")

def setup(bot):
    bot.add_cog(ErrorHandeling(bot))