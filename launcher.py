from lib.bot import bot
from keep_alive import keep_alive
version = "0.0.2"
keep_alive()
bot.run(version)