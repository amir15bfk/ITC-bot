import requests
import discord
import random
from .channels import Channels
from discord.ext import tasks, commands 
import os


#def randomChoice(list):
#    return random.choice(list)

API_KEY = os.environ['google-api-key']


URL = 'https://www.googleapis.com/youtube/v3/search?' # GOOGLE-API URL TO GET YOUTUBE VIDEOS


# CHANNELS THAT GONNA RECIVE RECOMMANDATIONS
DEV_DISCORD_CHANNEL = 865547748455743489 #'development-🖥'
DESING_DISCORD_CHANNEL = 865548466682986536#'desing-🖌'
PHY_DISCORD_CHANNEL = 865548596971438090#'science🔭'
ECO_DISCORD_CHANNEL = 865548605959962655#'other📜'


'''
PHY_CHANNLES:
    
    0: Stuff Made Here
    1: Nidhal Guessoum
    2: Veritasium
    3: 7osin Abdallah
    4: ScienceClic English
    5: Arvin Ash
    6: The Science Asylum
    7: Kurzgesagt – In a Nutshell
    8: Physics Girl
    9: minutephysics
    10: Parth G

'''


PHY_CHANNLES = ['UCj1VqrHhDte54oLgPG4xpuQ', 'UCxPtfAOwtyd_N6keP3MnVmw', 'UCHnyfMqiRRG1u-2MsSQLbXA', 
                
                'UCFq4pOuTiZmfJyCxaYTT3Hg', 'UCWvq4kcdNI1r1jZKFw9TiUA', 'UCpMcsdZf2KkAnfmxiq2MfMQ', 
                
                'UCXgNowiGxwwnLeQ7DXTwXPg', 'UCsXVk37bltHxD1rDPwtNM8Q', 'UC7DdEm33SyaTDtWYGO2CwdA', 
                
                'UCUHW94eEFW7hkUMVaZz4eDg', 'UC9lztld5qPi-6WZ9_QIVR6g']




'''
DEV_CHANNELS:

    0: LiveOverflow
    1: Dev Ed
    2: freeCodeCamp.org
    3: TechHut
    4: Fireship
    5: IAmTimCorey
    6: Google Developers
    7: DevTips
    8: Gaurav Sen
    9: Two Minute Papers
    10: MiCode
    11: Hesham Asem
    12: Siraj Raval
    13: Derek Banas

'''

DEV_CHANNELS = ['UClcE-kVhqyiHCcjYwcpfj9w', 'UClb90NQQcskPUGDIXsQEz5Q', 'UC8butISFwT-Wl7EV0hUK0BQ',
                'UCjSEJkpGbcZhvo0lr-44X_w', 'UCsBjURrPoezykLs9EqgamOA', 'UC-ptWR16ITQyYOglXyQmpzw', 
                'UC_x5XG1OV2P6uZZ5FSM9Ttw', 'UCyIe-61Y8C4_o-zZCtO4ETQ', 'UCRPMAqdtSgd0Ipeef7iFsKw',
                'UCbfYPyITQ-7l4upoX8nvctg', 'UCYnvxJ-PKiGXo_tYXpWAC-w',
                'UCxxljM6JkSvJVSD_T90ZnMw',
                'UCWN3xxRkmTPmbKwht9FuE5A',
                'UCwRXb5dUK4cvsHbx-rGzSgw']


'''
DESING_CHANNELS:

    0: XO PIXEL
    1: chunbuns
    2: DesignSense
    3: DesignCourse
    4: Cuberto Design

'''
DESING_CHANNELS = ['UC97rIjLDrO9ji6oAQsfgyiw', 'UClYfiU4L1Ry7R6sgpZ_F9PQ', 'UCK3KESgQlmEBJ5DnRxWJ9oA',

                   'UCVyRiMvfUNMA1UPlDPzG5Ow', 'UCzestFrXpwSGCfcbO2pObwQ']


'''
ECO_CHANNELS:

    0: I9tisad el kawkab
    1: The economist
    2: TED-Ed
    3: MokhbirEqtisadi

'''
ECO_CHANNELS = ['UCjMdgUQQM68S7tdXspE45Ag', 'UCrusF4_NrZbzLxtX0ZRfLEQ', 'UCsooa4yRKGN_zEE8iknghZA', 'UC4kRorAXuIkyIX6vwXKaLWg']




devChannels = Channels(urls=DEV_CHANNELS, discordChannel=DEV_DISCORD_CHANNEL)
ecoChannels = Channels(urls=ECO_CHANNELS, discordChannel=ECO_DISCORD_CHANNEL)
phyChannels = Channels(urls=PHY_CHANNLES, discordChannel=PHY_DISCORD_CHANNEL)
desingChannels = Channels(urls=DESING_CHANNELS, discordChannel=DESING_DISCORD_CHANNEL)



channelSelector = [0, 1, 2, 3]

def get_video(url, params):
    r = requests.get(url=url, params=params)
    data = r.json()
    item = random.choice(data['items'])
    return item

def get_recom(): 
    channels = ''
    selectedChannel = random.choice(channelSelector)

    if (selectedChannel == 0): channels = devChannels
    elif (selectedChannel == 1): channels = ecoChannels
    elif (selectedChannel == 2): channels = phyChannels
    elif (selectedChannel == 3): channels = desingChannels

    CHANNEL = channels.getRandomChannel()
    #print(CHANNEL)


    PARAMS = {

      'key': API_KEY,
      'channelId': CHANNEL,
      'part': 'snippet,id',
      'order': 'date',
      'maxResults': '20'

    }

    try:
        video = get_video(URL, PARAMS)
    except Exception as ex:
        print(ex.message)
        return

    video = get_video(URL, PARAMS)

    videoId = video['id']['videoId']

    videoUrl = f'https://www.youtube.com/watch?v={videoId}'
    print(videoUrl)

    snippet = video['snippet']
    publishedAt = snippet['publishedAt']
    title = snippet['title']
    description = snippet['description']
    thumbnail = snippet['thumbnails']['default']['url']
    channelTitle = snippet['channelTitle']

    
    
    news_card=discord.Embed(title=title, url=videoUrl, description=description, color=0x3bcbff)
    news_card.set_thumbnail(url=thumbnail)
    news_card.set_author(name=channelTitle)
    news_card.set_footer(text='YouTube')
    news_card.add_field(name='Date', value=publishedAt)
    return channels.discordChannel,news_card,videoUrl
