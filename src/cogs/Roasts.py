from . import phrases

from discord.ext import commands

class roasts(commands.Cog,name='Roasts',):
	"""Use to roast some one"""
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command()
	async def roast(self,ctx,x,y):
		'''Roast someone usage: so roast @user[or object] [noun/word]'''
		roast = phrases.get_so_insult_with_action_and_target(x, y)
		await ctx.send(str(roast))
		

	@commands.command()
	async def sinsult(self,ctx,x):
		"""Simply insult someone usage: so insult @user"""
		insult = phrases.get_simple_insult(x)
		await ctx.send(str(insult))

	@commands.command()
	async def insult(self,ctx,x):
		'''Norime Insult'''
		insult = phrases.get_so_insult(x)
		await ctx.send(str(insult))

	@commands.command()
	async def insulta(self,ctx,x,y):
		"""Insult Some one With a Action"""
		insult = phrases.get_so_insult_with_action(x,y)
		await ctx.send(str(insult))

def setup(bot):
	bot.add_cog(roasts(bot))