import discord
from discord.ext import commands

class Dev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def debug(ctx,self):
        '''Toggles debug mode'''
        if debugstate == False:
            self.bot.load_extension('jishaku')
            print("[cyan] Debug mode enabled[/cyan]")
            await ctx.send('Debug mode enabled')
            debugstate = True

        elif debugstate == True:
            self.bot.unload_extension('jishaku')
            print("[yellow]Debug mode disabled[/yellow]")
            await ctx.send('Debug mode disabled')
            debugstate = False



def setup(bot):
    bot.add_cog(Dev(bot))