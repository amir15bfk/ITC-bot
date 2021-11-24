
import os
import discord
import requests
from keep_alive import keep_alive

client = discord.Client()
TOKEN = os.environ['TOKEN']

@client.event
async def on_message(message):

  if message.content.startswith('>IT'):
    await message.channel.send('CCCCCCC!:fire:')

keep_alive()
client.run(TOKEN)