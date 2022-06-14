import discord
from memeGenerator import memeGenerator

with open('token.txt','r',encoding='utf8') as tokenfile:
    token = tokenfile.read().strip()

bot = discord.Bot(prefix='.',intents=discord.Intents.all())

@bot.event
async def on_ready():
    pass

@bot.event
async def on_message(message):
    if message.content.startswith(',gen'):
        await message.reply(file=discord.File('maxresdefault.jpeg'))

bot.run(token)