import random
class Channels:
    
    def __init__(self, urls, discordChannel) -> None:
        self.urls = urls
        self.discordChannel = discordChannel

    def getRandomChannel(self):
        return random.choice(self.urls)