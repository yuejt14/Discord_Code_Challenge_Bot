import os
import re
import discord
from discord.ext import commands, tasks
from src.leetcode_client import LeetCodeClient
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=commands.when_mentioned, intents=intents)

leetcode_client = LeetCodeClient()


@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')
    print('----------')

    from config import channels
    general = bot.get_channel(channels.get('general'))
    await general.send('Haker Bot is online')


# @bot.command()
# async def cookies(ctx):
#     await ctx.send('Refreshing Cookie Tokens...')
#     submit_message_pattern = r'```(?P<lang>\S+)\n(?P<code>[\s\S]*)```'
#
#
#
#     # LeetCodeClient.refresh_cookies()




@bot.command()
async def submit(ctx):
    await ctx.send('Received submission, please wait for your result...')

    submit_message_pattern = r'```(?P<lang>\S+)\n(?P<code>[\s\S]*)```'
    m = re.search(submit_message_pattern, ctx.message.clean_content)

    if not bool(m):
        await ctx.send("Invalid cold format! Please send code in the following format:\n" +
                       "\\`\\`\\`language\n #your code\n \\`\\`\\`")
        return

    code = m.group('code')
    lang = m.group('lang')
    submission = leetcode_client.submit(m.group('code'), m.group('lang'))
    result = leetcode_client.submit_and_check(code, lang)

    await ctx.send(result)


@bot.command()
async def start(ctx):
    print("starting loop")
    repeating_task.start()


@tasks.loop(seconds=10)
async def repeating_task():
    channel = bot.get_channel(1044738969352536126)
    await channel.send("repeating message")


@repeating_task.before_loop
async def before_repeating_task():
    await bot.wait_until_ready()


bot.run(os.getenv('DISCORD_TOKEN'))
