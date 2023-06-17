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

grup = 'mapiamodcuu'
bot_id = 'TrueMafiaBot'
lanjut = '/next@TrueMafiaBot'
quit = '/quit'
game = '/game@TrueMafiaBot'
start = '/start@TrueMafiaBot'
lanjut = '/next@TrueMafiaBot'
kirim = 'Turu'

kon = 0

async def bentar(w):
    await asyncio.sleep(w)
    
with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(-1001492059055 , lanjut))
    @client.on(events.NewMessage(incoming=True, from_users=bot_id))
    async def handle_chat(event):
        pesan = event.raw_text
        global kon
        
        
        if "Perhatian!" in pesan:
            await event.click(0)
            print(time.asctime(), 'Game baru')
            return
        
        if "Anda adalah" in pesan:
            print(time.asctime(), pesan)
            return
        
        if "Permainan sudah dimulai..." in pesan:
            time.sleep(3)
            await client.send_message(-1001492059055,lanjut)
            print(time.asctime(), 'Lanjut')
            return
          
        if "Siapa yang ingin Anda lynch?" in pesan:
            time.sleep(3)
            await client.send_message(-1001492059055,kirim)
            print(time.asctime(), 'Lanjut')
            return
              
        if "Permainan telah berakhir" in pesan:
            time.sleep(1)
            await client.send_message(-1001492059055,lanjut)
            print(time.asctime(), pesan)
            return
        

        
    @client.on(events.NewMessage(chats=-1001492059055))
    async def handler(event):
        pesan = event.raw_text
        
        if "Jumlah minimum pemain - 4" in pesan:
            print(time.asctime(), pesan)
            await bentar(2)
            await client.send_message(-1001492059055, lanjut)
            return
          
        
                
    client.start() 
    print(time.asctime(), 'Mulai...')
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')
	