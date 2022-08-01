from ast import alias
import discord
from discord.ext import commands
from to import Token

bot = discord.Client()

@bot.event
async def on_ready():
    print("==============")
    print("logged in")  #화면에 봇의 아이디, 닉네임 출력
    print(bot.user.name)
    print("==============")
    # 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
    # 이 기능을 이용하여 봇의 상태를 간단하게 출력 가능합니다.
    game = discord.Game("정이라고 하자")
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.event
async def on_message(message):
    # 받은 메시지의 author 가 bot 인 경우 return
    if message.author.bot:
        return None

    # 답장할 채널은 메세지 받은 채널로 설정
    channel = message.channel
    msg = message.content
    if (msg[0]=='정' and len(msg) == 1):  
        await channel.send('얼빻') 
    else:
        for i in msg:
            if i =='김' :
              msg = msg.replace('김', '\'정\'')
              await channel.send(msg)    
              break
            if i =='정':
                msg = msg.replace('정',  '\'정\'')
                await channel.send(msg)
                break
             
bot.run(Token) #토큰