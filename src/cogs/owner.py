from discord.ext import commands


class Owner(commands.Cog,name="Owner"):
    """OOO says owner can use only"""

    def __init__(self, bot):
        self.bot = bot
    
    # Hidden means it won't show up on the default help.
    @commands.command(name='load',hidden=True)
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='unload',hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')


    # @commands.command(name='reload', hidden=True)
    # @commands.is_owner()
    # async def reload(self, ctx, *, cog: str):
    #     """Command which Reloads a Module.
    #     Remember to use dot path. e.g: cogs.owner"""

    #     try:
    #         self.bot.unload_extension(cog)
    #         self.bot.load_extension(cog)
    #     except Exception as e:
    #         await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
    #     else:
    #         await ctx.send('**`SUCCESS`**')

    @commands.command(name='reload',hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    # @commands.command(name='reload')
    # @commands.is_owner()
    # @commands.command(aliases=[""])
    # async def leave(ctx,arg1):
	#     to_leave = arg1
	#     await leave(to_leave)

def setup(bot):
    bot.add_cog(Owner(bot))