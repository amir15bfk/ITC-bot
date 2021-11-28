from discord import Intents
from discord import Embed,File
from datetime import datetime
from discord.ext.commands import Bot as BotBase
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.errors import HTTPException, Forbidden
from discord.ext.commands import (CommandNotFound, BadArgument, MissingRequiredArgument,
								  CommandOnCooldown)
from apscheduler.triggers.cron import CronTrigger

import os
import random
from ..db import db
from ..recom_bot import recom_bot


import tracemalloc

tracemalloc.start()

PREFIX = ">"
OWNER_IDS=[403096560914923531]
IGNORE_EXCEPTIONS = (CommandNotFound, BadArgument)
class Bot(BotBase):
  def __init__(self):
    self.PREFIX = PREFIX
    self.ready = False
    self.guild = None
    self.scheduler = AsyncIOScheduler()
    db.autosave(self.scheduler)
    
    super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS,
    itents=Intents.all())  
  def run(self,version):
    self.VERSION = version
    self.TOKEN = os.environ['TOKEN']
    print("running bot ...")
    super().run(self.TOKEN,reconnect=True)
  

  async def on_connect(self):
    print("bot connected")
  
  async def on_disconnect(self):
    print("bot disconnected")
    #channel = self.get_channel(860464413777330206)
    #await channel.send("i'm down :small_red_triangle_down:  ")

  async def on_ready(self):
    if not self.ready:
      self.ready =True 
      self.guild = self.get_guild(800009861982191617)
      bot.scheduler.add_job(self.sendRecommandations, CronTrigger(hour="8,18,20"))
      self.scheduler.start()
      print("bot ready")
      """
      channel = self.get_channel(800009862792609816)
      embed = Embed(title="update 0.0.4",description ="working now",color=0x00ff00,timestamp=datetime.utcnow())
      embed.add_field(name ="version",value=self.VERSION,inline=True)
      embed.add_field(name ="updates",value=" - we merge the ITC bot with youtube Recommendations bot \n- the ITC bot will send every day at (8 am,18 pm ,and 20 pm ) a youtube video in the Youtube Recommendation category",inline=True)
      embed.add_field(name ="note",value="if you want a contribute in me just contact amir",inline=False)
      embed.set_image(url=self.guild.icon_url)
      embed.set_author(name="IT community bot" , icon_url=self.guild.icon_url)
      embed.set_footer(text="by amir & hamza to ITC ❤️ ")
      """
      channel = self.get_channel(860464413777330206)
      embed = Embed(title="is Online",description ="the bot is live",color=0x00ff00,timestamp=datetime.utcnow())
      embed.add_field(name ="version",value=self.VERSION,inline=True)
      embed.set_author(name="IT community bot" , icon_url=self.guild.icon_url)
      embed.set_footer(text="by amir & hamza to ITC ❤️ ")
      await channel.send(embed=embed)
    else :
      print("bot reconnected")
  
  async def on_error(self, err, *args, **kwargs):
    if err == "on_command_error":
      await args[0].send("Something went wrong.")
      await self.stdout.send("An error occured.")
    raise
  
  async def on_command_error(self, ctx, exc):
    if any([isinstance(exc, error) for error in IGNORE_EXCEPTIONS]):
      pass
    elif isinstance(exc, MissingRequiredArgument):
      await ctx.send("One or more required arguments are missing.")
    elif isinstance(exc, CommandOnCooldown):
      await ctx.send(f"That command is on {str(exc.cooldown.type).split('.')[-1]} cooldown. Try again in {exc.retry_after:,.2f} secs.")
    elif hasattr(exc, "original"):
			# if isinstance(exc.original, HTTPException):
			# 	await ctx.send("Unable to send message.")
      
      if isinstance(exc.original, Forbidden):
        await ctx.send("I do not have permission to do that.")
      else:
        raise exc.original
    else:
      raise exc
  async def on_message(self,message):
    if message.content.lower()=='>it':
      n = random.randint(3, 15)
      emoje = [":fire:",":star2:",":sunglasses:" ,":loudspeaker:"]
      title='C'*n+'!'+emoje[random.randrange(len(emoje))]
      embed = Embed(title=title,color=0xff0000)
      await message.channel.send(embed=embed)
    elif message.content.upper()=='>L3LAM':
      embed = Embed(title="ITC The Best Ever !:fire:",color=0x00ff00)
      embed.set_author(name="IT community bot" , icon_url=self.guild.icon_url)
      file = File("/home/runner/ITC-BOT/data/other/itcccc.jpeg", filename="image.png")
      embed.set_image(url="attachment://image.png")
      embed.set_footer(text="itc family ")
      await message.channel.send(file=file,embed=embed)
  async def sendRecommandations(self): 
    channel,news_card,videoUrl =recom_bot.get_recom()
    channel = self.get_channel(channel)
    
    
    msg = await channel.send(embed=news_card)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')
    await msg.add_reaction('😂')
    await msg.add_reaction('😍')
    await msg.add_reaction('🤩')
    await msg.add_reaction('😯')
    await msg.add_reaction('😡')
    await msg.add_reaction('🔥')
    await msg.add_reaction('😠')
   
  


bot = Bot()