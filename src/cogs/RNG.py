import random
from discord.ext import commands
from rich import print
from rich.console import Console
console = Console()

class RNG(commands.Cog,name="RNG"):
    """It's a game of chance"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, dice : str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await self.bot.say('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for _ in range(rolls))
        await self.bot.say(result)

    @commands.command(description='For when you wanna settle the score some other way')
    async def choose(self, *choices : str):
        """Chooses between multiple choices."""
        await self.bot.say(random.choice(choices))
    @commands.command(aliases=["gu"])
    async def Guess(self, ctx):
        """Guess a number between 1 and 100"""
        number = random.randint(1, 100)
        print(f"[#d4af37]{number}[/#d4af37]")
        await ctx.send("Guess a number between 1 and 100")
        guess = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author)

        if int(guess.content) == number:
            await ctx.send("You guessed right!")
        else:
            await ctx.send("You guessed wrong!\nThe number was {}".format(number))


def setup(bot):
    bot.add_cog(RNG(bot))