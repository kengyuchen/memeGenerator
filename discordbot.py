from logging import exception
import discord
from memeGenerator import memeGenerator
from memeGenerator import remove_file
import random

with open('token.txt','r',encoding='utf8') as tokenfile:
    token = tokenfile.read().strip()

bot = discord.Bot(intents=discord.Intents.all())

errormsg = [
    'https://cdn.discordapp.com/attachments/985448312712880150/986651966258151434/unknown.png',
    'https://cdn.discordapp.com/attachments/985448312712880150/986655956165337138/unknown.png'
]

@bot.event
async def on_ready():
    print('ready')

@bot.event
async def on_message(message):
    if message.content.startswith('.gen'):
        #指令: .gen <句子> [關鍵字1],[關鍵字2],...... [排除字1],[排除字2]...... (如果要排除字就不可以沒有關鍵字) (排除字、關鍵字、句子均不可包含空格)
        breakdown = message.content.split(' ')
        while not len(breakdown) >= 4:
            breakdown.append(None)
        if not breakdown[3] == None:
            breakdown[3].split(',')
        if not breakdown[2] == None:
            breakdown[2].split(',')
        try:
            memeGenerator(breakdown[1],breakdown[2],breakdown[3],str(message.id))
            file = discord.File(f'phase3_{message.id}.png')
            await message.reply(file=file)
        except exception as e:
            await message.reply(errormsg[random.randrange(len(errormsg))])
            try:
                print(e)
            except:
                pass
        remove_file(f'phase3_{message.id}.png')

bot.run(token)