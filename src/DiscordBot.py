import discord
import random
import datetime
import time
from bisect import bisect
import os

from DiscordActions import *
from config import *

envs = {
    'development': Development,
    'test': Test,
    'production': Production,
}

isPlayerGaming = {}

def prob_choice(items, weights):
    total = weights[-1]
    hi = len(items) - 1
    return items[bisect(weights, random.random() * total, 0, hi)]


client = discord.Client(intents=discord.Intents.all())
env = envs[os.environ['ENVIRONMENT']]()

# botのステータスのアクティビティの管理
@client.event
async def on_ready():
    bot_activity_status = BotActivityStatusAction(client)
    await bot_activity_status.exec()()
    del bot_activity_status

# チャンネル入退室時の通知処理 
@client.event
async def on_voice_state_update(member, before, after):

    # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
    voise_channel_bot_send = BotSendAction(client.get_channel(int(os.environ['VOICE_CHAT_TEXT'])))

    # チャンネルへの入室ステータスが変更されたとき（ミュートON、OFFに反応しないように分岐）
    if before.channel != after.channel:

        # 入退室を監視する対象のボイスチャンネル（チャンネルIDを指定）
        announceChannelIds = [int(os.environ['AnnounceChannelId1']), int(os.environ['AnnounceChannelId2'])]

        inMember = [
            '__  が参加しました！おでけけ　おでけけ　ランラララン♪',
            '__  が参加しました！__{}__を知ると世界が平和に？'.format(member.name),
            '__  が参加しました！アーニャんちへ　いらさいませ！',
            '__  が参加しました！こ…ころしや…!!すぱい　ころしや　わくわくっ!!',
            "__  が参加しました！"
        ]
        inWeights = [1, 1, 1, 1, 96]

        outMember = [
            '__  が抜けました！あ～　アーニャ__{}__いなくて寂しい～'.format(member.name),
            '__  が抜けました！アーニャ売り飛ばされるー！'
            '__  が抜けました！アーニャおうちかえりたい',
            '__  が抜けました！ひとがごみのようだ',
            "__  が抜けました！",
        ]

        outWeights = [1, 1, 1, 1, 96]

        # 退室通知
        if before.channel is not None and before.channel.id in announceChannelIds:
            randint = random.randrange(0, len(outMember))
            # await botRoom.send("**" + before.channel.name + "** から、__" + member.name + prob_choice(outMember, outWeights))
        # 入室通知
        if after.channel is not None and after.channel.id in announceChannelIds:
            randint = random.randrange(0, len(inMember))
            await voise_channel_bot_send.exec()("**" + after.channel.name + "** に、__" + member.name + prob_choice(inMember, inWeights))

        del voise_channel_bot_send

# Botのトークンを指定（デベロッパーサイトで確認可能）
client.run(env.get_token())