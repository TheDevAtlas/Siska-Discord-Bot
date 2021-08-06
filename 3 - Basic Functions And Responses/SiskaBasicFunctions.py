# Jacob McGowan 2021 #
# Parse Messages For Symbol Than Respond #

import discord
import os
from dotenv import load_dotenv
import random

client = discord.Client()

load_dotenv()
TOKEN = 'DISCORD TOKEN'

# Fact Of The Day List #
fotd = [
    'Emus Won The War In Austrailia',
    'Bird Digest Bone, Because Board',
    'Humming Bird Has Fazt Heart Go Brrrrrrrr',
    'Lizard Has Snake With Leg',
    'Types Of Birds Can Be Poisonous To Touch',
    'Coding Is Weird',
    'Discord Server Is Now In Termoil',
    'Java Is The Only Coding Language That Is Pure Coffee',
    'Desposito Play Country Roads',
    'The End Is Neigh, The Code Ninjas Minecraft Server Has Been Reformed. The Wheat Empire Will Return'
]

@client.event
async def on_message(message):
    # Don't Run The Code For Messages Sent By Bot #
    if message.author == client.user:
        return

    # Parse Message To Find Command #
    if message.content.count("!") > 0:
        if message.content == "!fact":
            await message.channel.send(fotd[random.randint(0,len(fotd)-1)])
        if message.content == "!update":
            await message.channel.send("Update Every Frame Breaks The Game!")
    
    # Parse Message For Days Of The Week #
    if message.content.count('monday') > 0:
        await message.channel.send("Only On A Tuesday!")
    if message.content.count('wednesday') > 0:
        await message.channel.send("Only On A Tuesday!")
    if message.content.count('thursday') > 0:
        await message.channel.send("Only On A Tuesday!")
    if message.content.count('friday') > 0:
        await message.channel.send("Only On A Tuesday!")
    if message.content.count('saterday') > 0:
        await message.channel.send("Only On A Tuesday!")
    if message.content.count('sunday') > 0:
        await message.channel.send("Only On A Tuesday!")

client.run(TOKEN)
