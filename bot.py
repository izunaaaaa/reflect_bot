import discord

bot = discord.Client()

# from to import Token
import time
from discord.ext import tasks
from datetime import timedelta
from datetime import datetime
import re

import os

Token = os.environ.get('BOT_TOKEN')


chat_list = []
check = 0



@tasks.loop(seconds=1)
async def check_time():
    current_time = datetime.now() + timedelta(hours=9)
    print (current_time)
    global check
    global chat_list
    if(current_time.hour == 23 and current_time.minute == 59 and current_time.second==00):
        channel = bot.get_channel(509635293175873538)
        await channel.send('주연이의 하루 기록')
        await channel.send(chat_list)
    if (current_time.hour ==13 and current_time.minute== 0 and current_time.second==00):
        channel = bot.get_channel(509635293175873538)
        await channel.send('지금 몇시냐?')
    if (current_time.hour ==13  and current_time.minute==4 and current_time.second==0):
        channel = bot.get_channel(509635293175873538)
        await channel.send('지금 몇시 몇분이냐?')

    if (current_time.hour==00 and current_time.minute==0 and current_time.day==13 and current_time.second==00):
        channel = bot.get_channel(509635293175873538)
        await channel.send('주연 생일 축하해')
    if(current_time.hour==0 and current_time.minute==0):
        check = 0
        chat_list = []


@bot.event
async def on_ready():
    print("==============")
    print("logged in")  
    print(bot.user.name)
    print("==============")
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

    if (m := re.match(r"^<a?:[\w]+:([\d]+)>$", message.content)):
        if message.content.startswith("<a:"):
            ext = "gif"
        else:
            ext = "png"
            
        embed = discord.Embed(color=message.author.color)
        embed.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
        embed.set_image(url=f"https://cdn.discordapp.com/emojis/{m.group(1)}.{ext}")
        emoji_msg = await message.channel.send(embed=embed)
        await emoji_msg.add_reaction(msg)
        await message.delete()



    if (message.author.name == 'zghik5'):
        global chat_list
        chat_list.append(msg)

    if (message.author.name == 'zghik5' and current_time.hour > 8 ):
         global check
         if (check == 0):
           await channel.send('주연 지금 일어났냐?')
         check = 1
    if ('정이라고하자' in msg or '정이라고 하자' in msg):
         await channel.send('\"그건 사랑이 아냐 그건 미련이 아냐 그냥\"')
    elif('전역' in msg):
        now = datetime.now()
        date_compare = datetime.strptime("20230531","%Y%m%d")
        date_diff = date_compare - now
        hour = date_diff.seconds // 3600 + date_diff.days * 24
        min = date_diff.seconds // 60 + date_diff.days * 1440
        sec = date_diff.seconds + date_diff.days * 86400
        await channel.send(f"남궁하사 전역일까지 앞으로 {date_diff}.\n\t\t\t\t\t\t\t\t\t\t\t 정확히 {date_diff.days}일, {hour:,} 시간, {min:,} 분, {sec:,} 초.")
    elif ('주연이의 하루 기록' == msg):
         await channel.send(chat_list)
    elif ('몇일' in msg):
         await channel.send(datetime.strftime(current_time, '오늘은 %m월 %d일입니다.'))
         if (current_time.day == 13):
           await channel.send("주연 생일 축하해")
    elif ('중훈?' in msg or "신중훈" in msg):
         await channel.send("어그로;;")
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
    elif (msg=='정'):  
         await channel.send('중궈')
    elif ('김이라고하자' in msg):
         await channel.send('그냥 정이라고 하자')
    elif ('이준석아님' in msg ):
         await channel.send('나이스')
    elif (msg =='ㅇㅈ' or msg =='dw'):
         await channel.send('ㅇㅈ')
    elif (('씨발' in msg  or '병신' in msg or '시발' in msg) and message.author.name == 'zghik5'):
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
