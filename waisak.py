import time, asyncio, sys, random

from telethon import TelegramClient, events, utils, Button

api_id = 18850178 
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = input ('Akun: ')

lantai = input ('Lantai: ')

cmd = '/waisak2567BE_GuaTambang_' + str(lantai)
restore = '/restore'
bot = 'KampungMaifamX4Bot'

with TelegramClient(sesi_file, api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message(bot, cmd))
        
        @client.on(events.NewMessage(from_users=bot))
        async def handler(event):
            
            if 'Gua ini memiliki permukaan' in event.raw_text:
                time.sleep(5)
                await event.click(0,0)
                return
            
            elif 'Kamu mendapat sebuah' in event.raw_text:
                    a = event.raw_text
                    b = a.split('_')
                    c = ' '.join(b)
                    d = c.split()
                    e = d.index('Istirahat')
                    f = d[e+1]
                    time.sleep(e)
                    await event.click(0,0)
                    return 
                
            if 'Kamu masih terlalu lelah' in event.raw_text:
                    a = event.raw_text
                    b = a.split('_')
                    c = ' '.join(b)
                    d = c.split()
                    e = d.index('Tunggu')
                    f = d[e+1]
                    time.sleep(e)
                    await event.click(0,0)
                    return
            
        client.start() 
        print("Makro Started")
        client.run_until_disconnected() 
        print(time.asctime(), '-', 'berhenti')
	
