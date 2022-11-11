# This example requires the 'message_content' intent.

import discord
from discord.ext import commands, tasks

bot_token = ""
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send(f'hello {message.author}')


@tasks.loop(seconds=10)
async def call_every_minute():
    print("starting repeat message...")
    message_channel = client.get_channel('984150117504417833')
    print(f'Got Channel {message_channel}')
    await message_channel.send("Minute message")


@call_every_minute.before_loop
async def before():
    print('waiting...')
    await client.wait_until_ready()
    print("Finished waiting")


client.run(bot_token)
