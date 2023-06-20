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
sesi_file = input("Mau akun mana = ")

mese = f"""
\n modcu 

@kentutlalat
@origyu
@jjaeggyu
@lovvnilla
@Lunaaaurr
@breadnee
@Jikjind
@soft_kyu
@na_mahen
@gia4no"""

with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(grup , mese))
    @client.on(events.NewMessage(chats=-1001657805800))
    async def handle_chat(event):
        pesan = event.raw_text
        
        if "Tim pemenang: Polos" in pesan:
            time.sleep(2)
            await client.send_message(grup, mese)
            print(time.asctime(), 'Tag orang')
            return
    
    client.start() 
    print(time.asctime(), 'Mulai...')
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')