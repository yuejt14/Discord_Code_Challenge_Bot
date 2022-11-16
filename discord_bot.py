import re
import time

import discord
from discord.ext import commands, tasks

import leetcode_client
from config import token

intents = discord.Intents.default()

intents.message_content = True
bot = commands.Bot(command_prefix=commands.when_mentioned, intents=intents)


@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')
    print('----------')
    # repeating_task.start()


@bot.command()
async def test(ctx):
    print('Command invoked')
    await ctx.send("hello")


@bot.command()
async def submit(ctx):
    print("submitted")
    pattern = r'```(?P<language>\S+)\n(?P<code>[\s\S]*)```'
    m = re.search(pattern, ctx.message.clean_content)
    if not bool(m):
        await ctx.send("Invalid cold format! Please send code in the following format:\n" +
                       "\\`\\`\\`language\n #your code\n \\`\\`\\`")
        return
    submission = leetcode_client.submit(m.group('code'))
    time.sleep(5)
    result = leetcode_client.check_submission_result(submission)
    await ctx.send(result)

    # await ctx.send("language:" + m.group('language'))
    # await ctx.send("code:\n" + m.group('code'))


@tasks.loop(seconds=10)
async def repeating_task():
    print("repeating task started...")
    channel = bot.get_channel(984150117504417833)
    await channel.send("repeating message")


@repeating_task.before_loop
async def before_repeating_task():
    await bot.wait_until_ready()


bot.run(token)

