import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

sad_words = ["upppdsddd", "cabbrazzzz"]

starter_encouragements = [
    "Cheer up!", "Hang in there.", "You are a great person / bot!"
]

if "responding" not in db.keys():
    db["responding"] = True


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + " -" + json_data[0]["a"]
    return (quote)


def update_encouragements(encouraging_message):
    if "encouragements" in db.keys():
        encouragements = db["encouragements"]
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = [encouraging_message]


def delete_encouragment(index):
    encouragements = db["encouragements"]
    if len(encouragements) > index:
        del encouragements[index]
    db["encouragements"] = encouragements


@client.event
async def on_ready():

    print("=========================")
    print("다음으로 로그인 합니다 : ")
    print(client.user.name)
    print("접속 완료")
    game = discord.Game("?도움말 | hanelbot.tk")
    print("=========================")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    if msg.startswith("?하늘아 안녕"):
        quote = get_quote()
        await message.channel.send('안녕하세요!^^')

    if msg.startswith("?출석"):
        quote = get_quote()
        await message.channel.send('출석 돼었습니다')

    if msg.startswith("?하늘아 뭐해"):
        quote = get_quote()
        await message.channel.send('공부 하고 있어요^^')

    if msg.startswith("?하늘아 놀자"):
        quote = get_quote()
        await message.channel.send('공부하고 있을땐, 놀면 안돼요 ㅠㅠ')

    if msg.startswith("?하늘아 몇살"):
        quote = get_quote()
        await message.channel.send('저는 1살 이에요!')

    if msg.startswith("?하늘아 생일"):
        quote = get_quote()
        await message.channel.send('저는 2020년 2월 20일에 생겼습니다!')

    if msg.startswith("?하늘아 잘가"):
        quote = get_quote()
        await message.channel.send('아 ㅠㅠㅠㅠㅠ')

    if msg.startswith("?하늘아 추방"):
        quote = get_quote()
        await message.channel.send('죄송합니다 ㅠㅠ')

    if msg.startswith("?영어"):
        quote = get_quote()
        await message.channel.send(quote)

    if msg.startswith("?안녕"):
        quote = get_quote()
        await message.channel.send('안녕하세요!')

    if msg.startswith("?에러"):
        quote = get_quote()
        await message.channel.send('에러가 공유 돼었습니다. 공유해주셔서 감사합니다.')

    if message.content == '?도박':
        randomlist = ['꽝', '꽝', '꽝', '꽝', '꽝', '꽝','꽝', '꽝', '(PM8V8-JLJ1-6UYT-42VQF)이 코드을 받으셧다면 `jaewoolee82#2507`로 DM주세요!','꽝', '꽝', '꽝','꽝', '꽝', '꽝', '꽝','꽝', '꽝', '꽝', '꽝','꽝', '꽝', '꽝', '꽝','꽝', '꽝', '꽝', '꽝','꽝', '꽝', '꽝', '꽝','꽝', '꽝', '꽝', '꽝','꽝', '꽝', '꽝', '꽝','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','꽝','꽝', '꽝','꽝','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','(Y538P-57A8-LDPR-IMHQH)이 코드을 받으셧다면 `jaewoolee82#2507`로 DM주세요!','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','성공','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝','(6W2QJ-LYQA-8DAV-ZQN1G)이 코드을 받으셧다면 `jaewoolee82#2507`로 DM주세요!','꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝','꽝','꽝', '꽝','꽝','꽝','꽝', '꽝','꽝','꽝','꽝', '꽝','꽝','꽝','꽝', '꽝','꽝','꽝','꽝', '꽝','꽝','꽝','꽝', '꽝','꽝','꽝','꽝', '꽝','꽝','꽝','꽝', '꽝','꽝','꽝','꽝', '꽝','꽝','꽝','꽝', '꽝','꽝','꽝','꽝', '꽝','꽝','꽝','꽝', '꽝','꽝','꽝','꽝', '꽝','꽝','꽝','꽝', '꽝','꽝','꽝','꽝', '꽝','꽝','꽝','꽝', '꽝','꽝','꽝','꽝', '꽝','꽝','꽝','꽝', '꽝','꽝','꽝','꽝', '꽝','꽝','꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝', '꽝','꽝','(JLTFV-G23S-V6FH-F1B32)이 코드을 받으셧다면 `jaewoolee82#2507`로 DM주세요!', '꽝', '꽝','꽝', '꽝', '꽝', '꽝','(U2MYN-WC3J-OJMN-7906X)이 코드을 받으셧다면 `jaewoolee82#2507`로 DM주세요!', '꽝', '꽝', '꽝','꽝', '꽝', '꽝', '꽝']
        ran = random.randint(0, len(randomlist)-1)
        embed = discord.Embed(title=f"'{randomlist[ran]}' 이(가) 나왔습니다!")
        embed.add_field(name="결과", value=f"{randomlist[ran]}이(가) 나왔습니다!")
        await message.channel.send(embed=embed)

    if message.content.startswith("?도움말"):
       embed = discord.Embed(title="하늘이봇 도움말", description="봇의 모든 명령어입니다.", color=0x00ff00)
       embed.add_field(name="?하늘아 안녕", value="하늘이가 인사해줍니다.", inline=True)
       embed.add_field(name="?핑", value="현재 봇의 핑(속도)를 알려줍니다.", inline=False)
       embed.add_field(name="?도박", value="도박을 해서 다양한 것을 얻을수 있습니다.", inline=False)
       embed.add_field(name="?주사위", value="주사위를 돌림니다.", inline=False)
       embed.add_field(name="?초대링크", value="초대링크을 알려조요!", inline=False)
       embed.add_field(name="개발자", value="jaewoolee82#2507", inline=False)
       embed.add_field(name="테스터", value="jamong#6201, FLOWER#3687, 싸이코#7975", inline=False)
       embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/806076310278373446/bcbe140fd749ed61e6a1b4e52edb679a.png?size=128')
       await message.channel.send(embed=embed)

    if message.content.startswith("?정보"):
       embed = discord.Embed(title="봇 이름", description="하늘", color=0x00ff00)
       embed.add_field(name="봇 개발일", value="2021년 2월 20일", inline=True)
       embed.add_field(name="봇 버전", value="2.1.0V", inline=False)
       embed.add_field(name="봇 개발언어", value="python", inline=True)
       embed.add_field(name="지원 언어", value="한국어(영어 지원 불가)", inline=False)
       embed.add_field(name="봇 개발자", value="cloud1881#5528", inline=False)
       await message.channel.send(embed=embed)


    if msg.startswith("?hellothisisverification"):
        quote = get_quote()
        await message.channel.send('jaewoolee82#2507')

    if msg.startswith("?초대링크"):
        quote = get_quote()
        await message.channel.send('https://discord.com/oauth2/authorize?client_id=806076310278373446&permissions=8&scope=bot')

    if message.content == "?핑":
        la = client.latency
        await message.channel.send(f'지금 봇의 핑은 {str(round(la * 100))}ms 입니다.')

    if message.content == '?주사위':
        randomlist = ['1', '2', '3', '4', '5', '6']
        ran = random.randint(0, len(randomlist)-1)
        embed = discord.Embed(title=f"'{randomlist[ran]}' 가 나왔습니다!")
        embed.add_field(name="결과", value=f"{randomlist[ran]}가 나왔습니다!")
        await message.channel.send(embed=embed)
        #주사위

    if db["responding"]:
        options = starter_encouragements
        if "encouragements" in db.keys():
            options = options + db["encouragements"]

        if any(word in msg for word in sad_words):
            await message.channel.send(random.choice(options))

    if msg.startswith("?nothingmaking"):
        encouraging_message = msg.split("?new ", 1)[1]
        update_encouragements(encouraging_message)
        await message.channel.send("새로운 단어가 추가돼였습니다.")

    if msg.startswith("?nothing"):
        encouragements = []
        if "encouragements" in db.keys():
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)

    if msg.startswith("?responding"):
        value = msg.split("?responding ", 1)[1]

        if value.lower() == "true":
            db["responding"] = True
            await message.channel.send("Responding is on.")
        else:
            db["responding"] = False
            await message.channel.send("Responding is off.")
            
keep_alive()
client.run(os.getenv("TOKEN"))
