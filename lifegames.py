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

bot_id = '.'

bet = 'Bbet 5+36'

acak = (
'5+36',
'5+36',
'5+36',
)


judi = 0

async def bentar(w):
    await asyncio.sleep(w)
    
with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(-1001944528171 , bet))
    
    @client.on(events.NewMessage(chats=-1001944528171))
    async def handler(event):
        pesan = event.raw_text
        from_ = await event.client.get_entity(event.from_id)
        global judi
        
                
        if "🚓 Finns sepertinya kamu mencoba melanggar hukum.." in pesan:
            print(time.asctime(), pesan)
            await bentar(600)
            await client.send_message(-1001944528171, bet)
            return
          
       
        if "🎰 📸 Finns [𝐒𝐕𝐇𝟑𝟏]ᴰ¹ #EcoleDeMode telah bertaruh" in pesan:
            print(time.asctime(), pesan)
            await bentar(2)
            await client.send_message(-1001944528171, "Bbet "+str(random.choice(acak)))
            return


        elif not from_.bot and 'cuan' in pesan or 'Cuan' in pesan:
            print(time.asctime(), pesan)
            await bentar(2)
            await event.reply('0pay *')
            return
        
          
                
    client.start() 
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')
	
	