import discord
import os
from dotenv import load_dotenv
import random

client = discord.Client()

load_dotenv()
TOKEN = 'ODcwNjUxMDQyMzE5MTcxNjI0.YQP2-A.KaOkK-2CSEG5d2G2ntkkAQvxu5c'

#########################3
@client.event
async def on_message(message):
    #if message.author == client.user:
    #    return


    #if message.content == '99!':
    #    response = random.choice(brooklyn_99_quotes)
    #    await message.channel.send(response)
    #else:
        
    response = message.content
    await message.channel.send(response)
############

client.run(TOKEN)
