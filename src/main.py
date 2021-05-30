import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return

  if msg.content.startswith('$hello'):
    await msg.channel.send('Hey there!')

client.run(os.getenv('TOKEN'))