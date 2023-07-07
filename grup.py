import time, os
import asyncio
import sys, re
import random
from time import sleep
from random import randint
from datetime import datetime
from telethon import TelegramClient, events, utils, Button
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = 'Finnkent'

liss = [
    '#TLF07',
    '#TLF08',
    '#TLF09',
    '#TLF010',
    '#TLF011',
    '#TLF012',
    '#TLF013',
    '#TLF014',
    '#TLF015',
]

lis = 0

with TelegramClient(sesi_file, api_id, api_hash) as client:
    @client.on(events.NewMessage(chats=-1001670658022))
    async def handler(event):
        pesan = event.raw_text
        global lis

        if "Waktu Menjawab : 30 menit" in pesan:
            await event.reply(str(liss[lis]) + ' Pengabdi Setan (2017)')
            lis += 1
            if lis >= len(liss):
                lis = 0
                
    client.start()
    print(time.asctime(), '-', 'Mulai...')
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Berhenti')