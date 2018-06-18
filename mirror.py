import discord
import time
import random

TOKEN = 'NDU4MzEwMTE0NDEyMTk5OTQ2.Dgl1-Q.-f6XPRc7Yu5vc-e9_wc8_XreUnw'

client = discord.Client()



@client.event 
async def on_message(message):
    if message.author == client.user:
        return
    rng = random.randint(1,4)
    
    if message.content.startswith('!pick'):
        if rng == 1:
            msg = 'dan'.format(message)
            await client.send_message(message.channel, msg)
        elif rng == 2:
            msg = 'casey'.format(message)
            await client.send_message(message.channel, msg)
        elif rng == 3:
            msg = 'jeff'.format(message)
            await client.send_message(message.channel, msg)    
        elif rng == 4:
            msg = 'richard'.format(message)
            await client.send_message(message.channel, msg)
  
@client.event
async def on_ready():
    print('Mir\'Ror active')
    print(client.user.name)
    print(client.user.id)
    print('-----')
    
client.run(TOKEN)
    