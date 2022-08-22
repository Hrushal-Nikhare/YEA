from ast import alias
import traceback
import discord
import asyncio
import contextlib
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.errors import Forbidden
from pretty_help import DefaultMenu, PrettyHelp
from rich import print
from rich.console import Console
import logging
import sys
# from discord_slash import SlashCommand
# from slash_help import SlashHelp


console = Console()
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
client = discord.Client()

intents = discord.Intents.all()



initial_extensions = [
					'cogs.simple',
					'cogs.members',
					'cogs.owner',
					'cogs.Roasts',
					'cogs.General',
					'cogs.RNG',
					'cogs.Moderation',
					'cogs.Music',
					'cogs.Fun',
					'cogs.dev',
					'cogs.Currency'
					]



def get_prefix(bot, message):
	"""A callable Prefix for our bot. This could be edited to allow per server prefixes."""

	# Notice how you can use spaces in prefixes. Try to keep them simple though.
	prefixes = ['!', '.','so ', 'So ', 'SO ','sO']

	# Check to see if we are outside of a guild. e.g DM's etc.
	if not message.guild:
		# Only allow ? to be used in DMs
		return '.'

	# If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
	return commands.when_mentioned_or(*prefixes)(bot, message)

# to invite https://discord.com/oauth2/authorize?client_id=951429657977323580&permissions=515396589568&scope=bot%20applications.commands

TOKEN = ""
# activity = discord.Game(name=f".help in {len(client.guilds)} servers!")
activity = discord.Game(name=".help in 5 servers!")

# await client.change_presence(status = discord.Status.idle, activity=activity)
bot = commands.Bot(command_prefix=get_prefix,description='Cybernetic', case_insensitive=True,intents=intents,activity=activity, status=discord.Status.do_not_disturb)
# slash = SlashCommand(bot, sync_commands=True)  # sync_commands=True preferred
# help_slash = SlashHelp(bot, slash, TOKEN, dpy_command=True, auto_create=True,prefix:".",)
no_category = "Default"
menu = DefaultMenu(page_left="◀", page_right="▶", remove="❌", active_time=60)
ending_note = "{ctx.bot.user.name} made by Shiny Eevee#7237 DM to report errors\nFor command {help.clean_prefix}{help.invoked_with}"
bot.help_command = PrettyHelp(menu=menu, ending_note=ending_note,no_category=no_category)

# #make a help command
# @bot.command(aliases=["help"])
# async def Help(ctx):

# Blocklist
blacklist = [953931668446674994]

# @client.command() 
@bot.listen()
async def block(ctx, arg1=None): 
	await ctx.message.delete()
	if ctx.author.id in blacklist: 
		await ctx.send("You are blacklisted") 
		return

# !non-command events


@bot.event
async def on_ready():
	print(f'\n[#94ceca]{bot.user} successfully logged in![#94ceca]')
	print(f'Connected to bot: [yellow] {bot.user.name}[/yellow]')
	print(f'Bot ID: {bot.user.id}')
	print('------------------------------------------------------')
	print('Successfully logged in and booted...!\n\n')
	
@commands.Cog.listener()
async def on_command_error(self, ctx, error):
	"""The event triggered when an error is raised while invoking a command.
	Parameters
	------------
	ctx: commands.Context
		The context used for command invocation.
	error: commands.CommandError
		The Exception raised.
	"""
	if hasattr(ctx.command, 'on_error'):
		return

	if cog := ctx.cog:
		if cog._get_overridden_method(cog.cog_command_error) is not None:
			return

	ignored = (commands.CommandNotFound, )
	error = getattr(error, 'original', error)

	if isinstance(error, ignored):
		return

	if isinstance(error, commands.DisabledCommand):
		await ctx.send(f'{ctx.command} has been disabled.')

	elif isinstance(error, commands.NoPrivateMessage):
		with contextlib.suppress(discord.HTTPException):
			await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
	elif isinstance(error, commands.BadArgument):
		if ctx.command.qualified_name == 'tag list':
			await ctx.send('I could not find that member. Please try again.')

	else:
		print(f'Ignoring exception in command {ctx.command}:', file=sys.stderr)
		traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


# @bot.event
# async def on_message(message):
# 	if message.author == bot.user:
# 		return
	
# 	if message.content.lower() == 'hello' or message.content.lower() == 'hi':
# 		await message.channel.send(f'Hi {message.author.mention}')
# 	if message.content.lower() == 'bye':
# 		await message.channel.send(f'Goodbye {message.author.mention}')
# 	if message.content.lower() == '!help':
# 		await message.channel.send(f'{message.author.mention} Check your DMs')
# 		await message.author.send(f'{bot.user.name} made by Shiny Eevee#7237 DM to report errors\nFor command {bot.command_prefix}{bot.help_command.invoked_with}')
# 	if message.content.lower() == 'good bot':
# 		await message.channel.send(f'Thanks {message.author.mention}')
# 	if message.content.lower() == 'bad bot':
# 		await message.channel.send(f'Sorry {message.author.mention}')
		
debugstate = False

# !commands
@commands.command(name="Restart",aliases=["FR",'ForceReload','restart'])
@commands.is_owner()
async def Restart(self, ctx):
	'''Restarts the bot'''
	await ctx.send("Restarting...")
	await self.bot.close()
	await self.bot.start(TOKEN)
	await ctx.send("Restarted")

@bot.command(name='info',aliases=['inf','i'])
async def info(ctx, *, member: discord.Member):
	"""Tells you some info about the member."""
	fmt = '{0} joined on {0.joined_at} and has {1} roles.'
	await ctx.send(fmt.format(member, len(member.roles)))

@info.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('I could not find that member...')

@bot.event
async def on_command_error(ctx, error):
   if isinstance(error, CommandNotFound):
    print(f"[red]{error}[/red]\n")
    
	
@bot.command(name="scrabble", aliases=["scrap,scrabblepoints"])
async def scrabble(ctx, arg):
	'''Scrabble score calculator'''
	# Key for point values of each letter
	score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
		 "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
		 "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
		 "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
		 "x": 8, "z": 10}
	points = sum(score[c] for c in arg)
	await ctx.send(points)

# @bot.command()
# async def load(ctx,extension_name : str):
#     """Loads an extension."""
#     try:
#         bot.load_extension(extension_name)
#     except (AttributeError, ImportError) as e:
#         await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
#         return
#     await ctx.send("{} loaded.".format(extension_name))

# @bot.command()
# async def unload(ctx,extension_name : str):
#     """Unloads an extension."""
#     bot.unload_extension(extension_name)
#     await ctx.send("{} unloaded.".format(extension_name))

@bot.command(name="prefixes", aliases=["p,pre"])
async def prefixes(ctx):
	"""Shows the current prefixes"""
	await ctx.send(f"Current prefixes: {bot.command_prefix}")

@bot.command(name='repeatme', aliases=['copyme', 'mimicme'],hidden=True)
@commands.is_owner()
async def repeatme(ctx,times : int, content='repeating...'):
	"""Repeats a message multiple times."""
	for _ in range(times):
		await ctx.send(content)

@bot.command(name='ping', aliases=['alive', 'pong'])
async def ping(ctx):
	"""Pong! Returns your websocket latency."""
	await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command(name='check', aliases=['online', 'oof'])
async def check(ctx):
	'''Check bot status'''
	embed = discord.Embed(
		description = f"I am online {ctx.author.mention}!",
		colour = discord.Colour.green()  
	)
	await ctx.send(embed=embed)

if __name__ == "__main__":
	print('[green]Starting bot...[/green]\n')
	print("")

	for extension in initial_extensions:
		try:
			bot.load_extension(extension)
			print(f'[green]Loaded {extension}[/green]')
		except Exception as e:
			exc = f'{type(e).__name__}: {e}'
			print('[red]Failed to load extension {}\n{}[/red]'.format(extension, exc))


	bot.run(TOKEN)

