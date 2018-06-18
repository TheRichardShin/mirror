import discord
import time
import random
TOKEN = '-------'
client = discord.Client()



@client.event 
async def on_message(message):
    if message.author == client.user:
        return
    rng = random.randint(1,4)
    
    if message.content.startswith('!pick'):
        if rng == 1:
            msg = 'Dan'.format(message)
            await client.send_message(message.channel, msg)
        elif rng == 2:
            msg = 'Casey'.format(message)
            await client.send_message(message.channel, msg)
        elif rng == 3:
            msg = 'Jeff'.format(message)
            await client.send_message(message.channel, msg)    
        elif rng == 4:
            msg = 'Richard'.format(message)
            await client.send_message(message.channel, msg)
  
@client.event
async def on_ready():
    print('Mir\'Ror active')
    print(client.user.name)
    print(client.user.id)
    print('-----')
    
client.run(TOKEN)
    