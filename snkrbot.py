import os 
import discord, requests, itertools


from discord.ext import commands
import json

from dotenv import load_dotenv 
from nike_module import get_nike_shoes, get_links


# load our local env so we dont have the token in public
intents = discord.Intents.default()
intents.members = True

#Command prefix
bot = commands.Bot(command_prefix="!", intents = intents)

def testhook():
    '''
    Sending a test Discord webhook notification
    '''

    print("hello")


#Nike SNKRS Lauch Calendar
NIKE_SNKRS_URL = 'https://www.nike.com/launch/?s=upcoming' 
 
#Creating a Session
s = requests.Session() 
#creating a Response
r = s.get(NIKE_SNKRS_URL) 


# Functions 
@bot.event 
async def on_ready(): 
    channel = bot.get_channel() #CHANNEL REMOVED FOR PRIVACY
    #Event Handler: Handles the event when the client  
    #has established a connection to Discord.
    embed=discord.Embed(title="Hello there! I am Botty Boi 2nd", url="http://joeltech.ddns.net", description="I hope that you are doing well and I would like to assist you as ur client  😎.", color=0xFF772D)
    embed.set_author(name="Joel.B", url="http://joeltech.ddns.net", icon_url="https://static.vecteezy.com/packs/media/components/global/search-explore-nav/img/vectors/term-bg-1-666de2d941529c25aa511dc18d727160.jpg")
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/f377126c-7717-4026-aa5b-7ca887157442")
    embed.add_field(name="Enter the following commands:", value="Type !nike if you want to view the 5 latest nike shoe releases on SNKRS. Or just chat by sending me a message such as !hello", inline=False) 
    embed.set_footer(text="(client  made by Joel Boi")
    await channel.send(embed=embed)
    print(f'{bot .user} has connected to Discord!') 
    print("webhook sent thru")

@bot.event
async def on_message(message): 
    '''client  replies back with sneaker info when it sees a command.'''
        
    #Ignore messages from the client  itself.
    if message.author ==  bot.user:
        return

    #!nike -> Give first five sneakers from Nike Launch Calendar
    if message.content.startswith('!nike'): 
        #check if the site is up
        if r.ok:
            shoes = get_nike_shoes()  #List of shoes and releases
            links = get_links()  #List of Links to shoes
            bot_message = ''  #The message the client  will send in chat

            for shoe, link in zip(shoes, links): 
                bot_message += shoe + '\n' + link + '\n\n'

            bot_message += 'For more Nike releases: ' + NIKE_SNKRS_URL
            await message.channel.send(bot_message) 
        else: 
            await message.channel.send('Nike site is down.')
            
    if message.content.startswith('!hello'): 
        # Check if the site is up
            msg= "Greetings!"
            await message.add_reaction('👍')
            await message.channel.send(msg)

    if message.content.startswith('!nice1'): 
    # Check if the site is up
            msg= "Sfe!"
            await message.add_reaction('👊')
            await message.channel.send(msg)        

if __name__ == '__main__':
    # Loads env variables from .env to shell's env variables 
    load_dotenv()  
    # Gets the token whic
    token = os.getenv('DISCORD_TOKEN') 
    # fiund token from .env
    bot.run(token)
                