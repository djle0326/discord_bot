import discord
from discord.ext import commands
import asyncio

TOKEN = 'private'  # 여기에 봇 토큰을 입력하세요.
GUILD_ID = private     # 여기에 서버 ID를 입력하세요.
CHANNEL_ID = private   #메시지를 보낼 채널의 ID

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

async def input_loop(channel):
    while True:
        msg = await bot.loop.run_in_executor(None, input, "Enter your message: ")
        if msg.lower() == "exit":
            break
        await channel.send(msg)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    channel = bot.get_channel(private)  #채널 ID를 입력
    bot.loop.create_task(input_loop(channel))

@bot.command(name='청소')
async def clear(ctx):
    await ctx.channel.purge(limit=100)
    await ctx.send('채팅이 정리되었습니다.')


bot.run(TOKEN)

