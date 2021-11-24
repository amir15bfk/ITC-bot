
import os
import discord
import requests
import random
from keep_alive import keep_alive

client = discord.Client()
TOKEN = os.environ['TOKEN']

@client.event
async def on_message(message):

  if message.content.startswith('>IT'):
    n= random.randint(3, 15)
    await message.channel.send('C'*n+'!:fire:')
    

keep_alive()
client.run(TOKEN)