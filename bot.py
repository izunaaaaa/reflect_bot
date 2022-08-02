import discord
# from to import Token
import time
from discord.ext import tasks
from datetime import datetime
import os

Token = 'MTAwMzUzMTM0MzM5ODk3NzU2Ng.GEhjeM._avt8M91QiWbiRKpKBFHDv7vj8m18r5m-6ZJR4'

bot = discord.Client()

@tasks.loop(seconds=1)
async def check_time():
    if (datetime.now().hour==13 and datetime.now().minute== 00 and datetime.now().second==00):
        channel = bot.get_channel(509635293175873538)
        await channel.send('지금 몇시냐?')
        time.sleep(200)
    elif (datetime.now().hour==13 and datetime.now().minute==4 and datetime.now().second==00):
        channel = bot.get_channel(509635293175873538)
        await channel.send('지금 몇시 몇분이냐?')
        time.sleep(30000)
    elif (datetime.now().hour==00 and datetime.now().minute==0 and datetime.now().date==13):
        channel = bot.get_channel(509635293175873538)
        await channel.send('주연 생일 축하해')
        time.sleep(30000) 

@bot.event
async def on_ready():
    print("==============")
    print("logged in")  #화면에 봇의 아이디, 닉네임 출력
    print(bot.user.name)
    print("==============")
    # 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
    # 이 기능을 이용하여 봇의 상태를 간단하게 출력 가능합니다.
    game = discord.Game("받아치기")
    check_time.start()
    await bot.change_presence(status=discord.Status.online, activity=game)


@bot.event
async def on_message(message):
    # 받은 메시지의 author 가 bot 인 경우 return
    if message.author.bot:
        return None
    # 답장할 채널은 메세지 받은 채널로 설정
    channel = message.channel
    msg = message.content
    print (msg)
    if ('정이라고하자' in msg or '정이라고 하자' in msg):
         await channel.send('/"그건 사랑이 아냐 그건 미련이 아냐 그냥/"')
    elif ('관악고' in msg):
         await channel.send('나도 관악고 피해자임')
    elif ('어그로' in msg or 'ㅇㄱㄹ' in msg):
         await channel.send('중훈?')
    elif ('너이준석' in msg or '너 이준석' in msg or '면 이준석' in msg or '면이준석' in msg):
         await channel.send('??????????') 
    elif (msg[0]=='정' and len(msg) == 1):  
         await channel.send('얼빻') 
    elif ('김이라고하자' in msg):
	       await channel.send('그냥 정이라고 하자')
    elif ('이준석아님' in msg ):
         await channel.send('나이스')
    elif (msg =='ㅇㅈ' or msg =='dw'):
         await channel.send('ㅇㅈ')
    elif (('씨발' in msg  or '병신' in msg) and message.author.name == 'zghik5'):
         await channel.send("주연 욕하지마")
    elif ('김' in msg and message.author.name=='zghik5'):
         msg = msg.replace('김', '\'정\'')
         await channel.send(msg)
    elif ('차단' in msg):
         embed=discord.Embed(title='차단하면 이준석', description='', color=0x00aaaa)
         embed.set_author(name="차단하지마",icon_url=message.author.avatar_url)
         await message.channel.send(embed=embed)
    return 


@bot.event
async def on_message_delete(message):
	if (message.author.name == 'zghik5'):
         msg = message.content
         channel = message.channel
         embed=discord.Embed(title=msg, description='', color=0x00aaaa)
         embed.set_author(name="주연이가 지운 메세지",icon_url=message.author.avatar_url)
         await message.channel.send(embed=embed)
         return

@bot.event
async def on_message_edit(before, after):
    if (before.author.name=='zghik5'):
         embed=discord.Embed(title=before.content + ' ->', description=after.content, color=0x00aaaa)
         embed.set_author(name="주연이가 수정한 메세지",icon_url=before.author.avatar_url)
         await before.channel.send(embed=embed)
         return

        
bot.run(Token) #토큰



