import time
import asyncio
import sys
import threading
from telethon import TelegramClient, events, utils

api_id = 18850178 
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = input("Mau akun mana = ")
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


mese = '/ia2023_Forest'
restore = "/restore_max_confirm"
restorecount = 0
maxrestore = 2
killer = maxrestore-1
abis = 0
total = 0

def masha2():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    with TelegramClient(sesi_file, api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message('KampungMaifamBot', mese))

        @client.on(events.NewMessage(from_users='KampungMaifamBot'))
        async def handler(event):
            global item, teks, emoji, butt
            teks = str(event)
            if 'Forest' in teks or 'Hutan' in teks:
                butt = []
                for item in teks.split():
                    if 'KeyboardButtonCallback' in item:
                        butt.append(list(item)[-3])
                for item in butt:
                    if butt.count(item)==2:
                        print(item)
                        time.sleep(8)
                        await event.click(butt.index(item))                        
                        return
                return
                
            if 'You get a' in event.raw_text or 'Berhasil mendapatkan' in event.raw_text:
                butt = []
                for item in teks.split():
                    if 'KeyboardButtonCallback' in item:
                        butt.append(list(item)[-3])
                for item in butt:
                    if butt.count(item)==2:
                        print(item)
                        time.sleep(8.5)
                        await event.click(text=item)                        
                        return
                return 
               

        client.run_until_disconnected()
        print(time.asctime(), '-', 'Stop')

threading.Thread(target=masha2).start()
print(time.asctime(), '-', 'Start')

#if abis == 2 :
#    client.disconnect()
#    clien.disconnect()
