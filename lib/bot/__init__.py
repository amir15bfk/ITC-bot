from discord import Intents
from discord import Embed
from discord.ext.commands import Bot as BotBase
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import os
import random

PREFIX = ">"
OWNER_IDS=[403096560914923531]
class Bot(BotBase):
  def __init__(self):
    self.PREFIX = PREFIX
    self.ready = False
    self.guild = None
    self.scheduler = AsyncIOScheduler()

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
    channel = self.get_channel(860464413777330206)
    await channel.send("i'm down :small_red_triangle_down:  ")

  async def on_ready(self):
    if not self.ready:
      self.ready =True 
      self.guild = self.get_guild(800009861982191617)
      print("bot ready")
      channel = self.get_channel(860464413777330206)
      embed = Embed(title="Now Online",description ="the bot is live",color=0x00ff00)
      embed.add_field(name ="version",value=self.VERSION,inline=True)

      await channel.send(embed=embed)
    else :
      print("bot reconnected")

  async def on_message(self,message):
    if message.content.lower()=='>it':
      n = random.randint(3, 15)
      emoje = [":fire:",":star2:",":sunglasses:" ,":loudspeaker:"]
      title='C'*n+'!'+emoje[random.randrange(len(emoje))]
      embed = Embed(title=title,color=0xff0000)
      await message.channel.send(embed=embed)


bot = Bot()