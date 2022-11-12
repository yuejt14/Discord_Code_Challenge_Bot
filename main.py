import discord
from discord.ext import commands, tasks
from config import token

intents = discord.Intents.default()

intents.message_content = True
bot = commands.Bot(command_prefix=commands.when_mentioned, intents=intents)


@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')
    print('----------')
    repeating_task.start()


@bot.command()
async def test(ctx):
    print('Command invoked')
    await ctx.send("hello")


@tasks.loop(seconds=10)
async def repeating_task():
    print("repeating task started...")
    channel = bot.get_channel(984150117504417833)
    await channel.send("repeating message")


@repeating_task.before_loop
async def before_repeating_task():
    await bot.wait_until_ready()


bot.run(token)

