import discord
# from to import Token
import time
from discord.ext import tasks
from datetime import timedelta
from datetime import datetime

import os

Token = os.environ.get('BOT_TOKEN')

check = 0



bot = discord.Client()

@tasks.loop(seconds=1)
async def check_time():
    current_time = datetime.now() + timedelta(hours=9)
    print (current_time)
    global check
    if (current_time.hour ==13 and current_time.minute== 0 and current_time.second==00):
        channel = bot.get_channel(509635293175873538)
        await channel.send('지금 몇시냐?')
    if (current_time.hour ==13  and current_time.minute==4 and current_time.second==0):
        channel = bot.get_channel(509635293175873538)
        await channel.send('지금 몇시 몇분이냐?')

    if (current_time.hour==00 and current_time.minute==0 and current_time.day==13):
        channel = bot.get_channel(509635293175873538)
        await channel.send('주연 생일 축하해')
    if(current_time.hour==0 and current_time.minute==0):
        check = 0


@bot.event
async def on_ready():
    print("==============")
    print("logged in")  #화면에 봇의 아이디, 닉네임 출력
    print(bot.user.name)
    print("==============")
    # print (datetime.now() + timedelta(hours=9)) 
    # 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
    # 이 기능을 이용하여 봇의 상태를 간단하게 출력 가능합니다.
    game = discord.Game("받아치기")
    check_time.start()
    await bot.change_presence(status=discord.Status.online, activity=game)


@bot.event
async def on_message(message):
    # 받은 메시지의 author 가 bot 인 경우 return
    if message.author.bot:
        print ("bot : " + message.content)
        return None

    # 답장할 채널은 메세지 받은 채널로 설정
    channel = message.channel
    msg = message.content
    current_time = datetime.now() + timedelta(hours=9)

    print ("user : " + msg)

    if (message.author.name == 'zghik5' and current_time.hour > 8 ):
         global check
         if (check == 0):
           await channel.send('주연 지금 일어났냐?')
         check = 1
    if ('정이라고하자' in msg or '정이라고 하자' in msg):
         await channel.send('\"그건 사랑이 아냐 그건 미련이 아냐 그냥\"')
    elif ('몇일' in msg):
         await channel.send(datetime.strftime(current_time, '오늘은 %m월 %d일입니다.'))
         if (current_time.day == 13):
           await channel.send("주연 생일 축하해")
    elif ("몇시몇분" in msg):
         await channel.send('지금은 ' + datetime.strftime(current_time, '%H시 %M분') +"입니다")
    elif ("몇분" in msg ):
         await channel.send('지금은 ' + datetime.strftime(current_time, '%M분') +"입니다")             
    elif ('몇시' in msg):
         await channel.send('지금은 ' +str(current_time.hour) +"시입니다")
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



