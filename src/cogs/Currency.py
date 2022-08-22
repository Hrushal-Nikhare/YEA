import aiohttp
import discord
from discord.ext import commands


class Currency(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["Cash","Money"])
    async def Bal(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.sheety.co/4251fde3384c28ffb26c6bf7d78add1d/dbCurrencyDatabase/sheet1") as r:
                r = await r.json()
                bal = r["sheet1"][0]["bal"]
                await ctx.send(f"{ctx.author.name}'s Balance is {bal}")


def setup(bot):
    bot.add_cog(Currency(bot))
