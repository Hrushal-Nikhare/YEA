from discord.ext import commands

class General(commands.Cog,name='General'):
    """General Commands"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='Usage: so square {number}', description='Usage: so square {number} \n used to square a number')
    async def square(self,ctx, arg): # The name of the function is the name of the command
        print(arg) # this is the text that follows the command
        await ctx.send(int(arg) ** 2) # ctx.send sends text in chat
    
def setup(bot):
    bot.add_cog(General(bot))