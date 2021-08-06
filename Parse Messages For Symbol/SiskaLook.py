# Jacob McGowan 2021 #
# Parse Messages For Symbol Than Respond #

import discord
import os
from dotenv import load_dotenv
import random

client = discord.Client()

load_dotenv()
TOKEN = 'DISCORD TOKEN'

lookFor = '?'

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.count(lookFor) > 0:
        await message.channel.send("IDK How To Answer That Question")

client.run(TOKEN)
