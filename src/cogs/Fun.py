from __future__ import unicode_literals
import discord
from discord.ext import commands
import random
from rich import print
from rich.console import Console
from discord.ext import commands
import random
import discord
import asyncio
import aiohttp
import json

import json
import io
console = Console()

class fun(commands.Cog,):
  """FUN STUFF"""
  def __init__(self, bot):
      self.bot = bot


  @commands.command(aliases=['8ball', 'ball'])
  async def _8ball(self, ctx, *, question):
          
    responses = ['As I see it, yes.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                'Don’t count on it.',
                'It is certain.',
                'It is decidedly so.',
                'Most likely.',
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Outlook good.',
                'Reply hazy, try again.',
                'Signs point to yes.',
                'Very doubtful.',
                'Without a doubt.',
                'Yes.',
                'Yes – definitely.',
                'You may rely on it.']
    q = f"Question: {question}"
    a = f"Answer: {random.choice(responses)}"
    embed = discord.Embed(
        title=(q),
        description=(a),
        colour=discord.Colour.blue()
    )

    await ctx.send(embed=embed)
          

  @commands.command(aliases=["facepalm"])
  async def fp(self, ctx):
            
    async with aiohttp.ClientSession() as session:
      async with session.get("https://www.reddit.com/r/facepalm/top.json") as response:
        j = await response.json()

    data = j["data"]["children"][random.randint(0, 25)]["data"]
    image_url = data["url"]
    title = data["title"]
    em = discord.Embed(description=f"[**{title}**]({image_url})", colour=discord.Colour.blue())
    em.set_image(url=image_url)
    em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
    await ctx.send(embed=em)

  @commands.command(aliases=["maymay", "memes"])
  async def meme(self, ctx):
            
    async with aiohttp.ClientSession() as session:
      async with session.get("https://www.reddit.com/r/memes/top.json") as response:
        j = await response.json()

    data = j["data"]["children"][random.randint(0, 25)]["data"]
    image_url = data["url"]
    title = data["title"]
    em = discord.Embed(description=f"[**{title}**]({image_url})", colour=discord.Colour.blue())
    em.set_image(url=image_url)
    em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
    await ctx.send(embed=em)

  @commands.command(aliases=['shoot','knockout'])
  async def KO(self, ctx,member):
                
                  gifslist =['https://media.tenor.com/images/e302b70e805f045816c100a92325b824/tenor.gif', 'https://media1.tenor.com/images/3da22c373b5506939514773ad496b170/tenor.gif?itemid=11751811', 'https://media1.tenor.com/images/b3dddda27a439a9951fdd0de5a0644e6/tenor.gif?itemid=15872871', 'https://media1.tenor.com/images/3b0d7cc04fb09adb1ccc96a23b98dd86/tenor.gif?itemid=6032176', 'https://media1.tenor.com/images/97248cf32942f467c4a049acbae8981e/tenor.gif?itemid=3555140', 'https://media1.tenor.com/images/c7dece5cdd4cee237e232e0c5d955042/tenor.gif?itemid=4902914']
                  gifs=random.choice(gifslist)
                  
                  embed = discord.Embed(
                      description=(f"{member} Has been Knocked Out!"),
                      colour=discord.Colour.blue()
                      )
                  embed.set_image(url=gifs)    
                  await ctx.send(embed=embed)

                  
  @commands.command()
  async def gunfight(self, ctx, user: discord.Member):
    global response
    choices = ['fire', 'draw', 'shoot', 'bang', 'pull', 'boom']
    gun = random.choice(choices)
    if ctx.message.author == user:
      await ctx.send("**You can't fight yourself!**")
    else:
      await ctx.send(f"{user.mention} **Do you accept the challenge?** ``yes``** or** ``no``?")     
    
    
    channel = ctx.channel.id

    def check (m):
      return m.channel == ctx.channel and m.author == user
    
    if ctx.message.author != user:                  
      try:
        response = await self.bot.wait_for('message', check=check, timeout=15)
      except:
        await ctx.send(f"**Looks like {user.mention} doesn't want to play :frowning:**")
    tr = random.randrange(5)
    
    if response.content.lower() == "yes":
        await ctx.send(f"{user.mention} **has accepted the challenge**  :slight_smile:")
        await asyncio.sleep(2)
        await ctx.send("**Get Ready, it will start at any moment!**")
        await asyncio.sleep(tr)
        await ctx.send(f"**Type** ``{gun}`` **now!**")

    

    if response.content.lower() == "no":         
        await ctx.send(f"{user.mention} has declined your request :frowning:")

    user1 = ctx.author
    user2 = user
    
    def check(n):
      return n.author in [user1, user2]

    message = await self.bot.wait_for("message", check=check)
    if message.author == user1:
      if message.content == gun:
        await ctx.send(f"{user1.mention} **Has Won!**")
        with open('scores.json','w+') as f:
          json.dump(str(user2.id), str(+1))
    else:
      if message.content == gun:
        await ctx.send(f"{user2.mention} **Has Won!**")
        with open('scores.json','w+') as f:
          json.dump(str(user2.id), str(+1))


  # @commands.command(aliases=["imbored", "im", "ib"])
  # async def bored(self, ctx):
  #   BoredAPI = requests.get('https://www.boredapi.com/api/activity')
  #   BoredJson = BoredAPI.json()
  #   print('\n'.join(f'{key.capitalize()}: {value}' for key, value in BoredJson.items()))
  #   await ctx.send('\n'.join(f'{key.capitalize()}: {value}' for key, value in BoredJson.items()))

  @commands.command(aliases=["imbored", "im", "ib"])
  async def bored(self, ctx):
    async with aiohttp.ClientSession() as cs:
     async with cs.get('https://www.boredapi.com/api/activity') as r:
        res = await r.json()  # returns dict
        await ctx.send('\n'.join(f'{key.capitalize()}: {value}' for key, value in res.items()))
  
  @commands.command(aliases=["sohungry", "imhungry","food"])
  async def hungry(self, ctx):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://www.themealdb.com/api/json/v1/1/random.php') as r:
        res = await r.json()
        msg = f"Name: {res['meals'][0]['strMeal']}\nCatorgy: {res['meals'][0]['strCategory']}\nArea: {res['meals'][0]['strArea']}\nYoutube: {res['meals'][0]['strYoutube']}"
        pic = f"\n{res['meals'][0]['strMealThumb']}"
        await ctx.send(msg+pic)
  
  @commands.command(aliases=["Foodpicture", "foodpics"])
  async def foodpic(self, ctx):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://foodish-api.herokuapp.com/api/') as r:
        res = await r.json()
        await ctx.send(res['image'])

  @commands.command(aliases=["morCoffee", "coffeepic"])
  async def Coffee(self, ctx):
      async with aiohttp.ClientSession() as cs:
        async with cs.get('https://coffee.alexflipnote.dev/random.json') as r:
          res = await r.json()
          await ctx.send(res["file"])

  @commands.command(aliases=["pictures", "pic"])
  async def pics(self, ctx):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://api.unsplash.com/photos/random/?client_id=NxvL9H3kJvXmnB1AoMajm-W4-mdqEoFiDHyZ2lSMOTI') as r:
        res = await r.json()
        pic = res['urls']['full']
        author = res['user']['name']
        await ctx.send(f'{pic} ')
        await ctx.send(f'By: {author}')
  
  @commands.command(aliases=["Shibepicture"])
  async def Shibe(self, ctx):
      async with aiohttp.ClientSession() as cs:
        async with cs.get('https://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true') as r:
          res = await r.json()
          await ctx.send(res[0])

  @commands.command(aliases=["dogpic"])
  async def dog(self, ctx):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://dog.ceo/api/breeds/image/random') as r:
        res = await r.json()
        await ctx.send(res['message'])

  @commands.command(aliases=["catpic"])
  async def cat(self, ctx):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://api.thecatapi.com/v1/images/search') as r:
        res = await r.json()
        await ctx.send(res[0]['url'])

  @commands.command(aliases=[])
  async def dogfact(self, ctx):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://dog-api.kinduff.com/api/facts') as r:
        res = await r.json()
        await ctx.send(res['facts'][0])

  @commands.command(aliases=[])
  async def catfact(self, ctx):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://catfact.ninja/fact') as r:
        res = await r.json()
        await ctx.send(res['fact'])

  @commands.command(aliases=["RandomAnimal", "Animal"])
  async def AnimalPic(self, ctx):
      async with aiohttp.ClientSession() as cs:
        async with cs.get('https://zoo-animal-api.herokuapp.com/animals/rand') as r:
          res = await r.json()
          await ctx.send(res['name']+'\nFound:'+res['geo_range']+'\nDiet:'+res['diet'])
          await ctx.send(res['image_link'])

  @commands.command(aliases=[])
  async def trump(self, ctx):
      async with aiohttp.ClientSession() as cs:
        async with cs.get('https://api.whatdoestrumpthink.com/api/v1/quotes/random') as r:
          res = await r.json()
          await ctx.send(res['message'])

  # @commands.command(aliases=[])
  # async def joke(self, ctx):
  #     async with aiohttp.ClientSession() as cs:
  #       async with cs.get('https://icanhazdadjoke.com/') as r:
  #         res = await r.json()
  #         await ctx.send(res['joke'])

  @commands.command(aliases=["exam",'excuses'])
  async def excuse(self, ctx):
      async with aiohttp.ClientSession() as cs:
        async with cs.get('https://excuser.herokuapp.com/v1/excuse') as r:
          res = await r.json()
          await ctx.send(res[0]["excuse"]+"\nCategory:"+res[0]["category"])


def setup(bot):
    bot.add_cog(fun(bot))
