#!/usr/bin/env python3
import time, asyncio, sys


from telethon import TelegramClient, events, utils, Button

api_id = 18850178 
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = input('Mau akun mana = ')

dest =('KampungMaifamXBot')
Ternak = '/pelihara_BayiBabi_155'
#restore = '/restore'
restore = '/restore_max_confirm'
 
with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(dest, Ternak))

    @client.on(events.NewMessage(from_users='KampungMaifamXBot'))
    async def handler(event):
        pesan = event.raw_text
        
        if "Berhasil menambahkan" in pesan or "Kandang ternak khusus penuh" in pesan:
            print('Isi kandang')
            time.sleep(2)
            await event.respond('/ambilHewan')
            return
        
        if "Kamu berhasil mendapat" in pesan:
            print('Ambil hasil')
            time.sleep(2)
            await event.respond(Ternak)
            #await event.respond('/act_WildBreeder')
            return
       
        #if "WildBreeder" in pesan:
            #time.sleep(2)
            #print(pesan)
            #await event.click(text="Claim")
            #await event.respond(Casino)
            #return
        
        if "Kamu tidak memiliki cukup energi" in pesan:
             print('Energi habis')
             time.sleep(2)
             await event.respond(restore)
             print(time.asctime(), 'Isi Ulang Energi')
             return
                
        if "Energi berhasil" in pesan:
            print('Energi pulih')
            time.sleep(2)
            await event.respond(Ternak) 
            return

    @client.on(events.NewMessage(chats=-1001944528171))
    async def handler(event):
        pesan = event.raw_text
        from_ = await event.client.get_entity(event.from_id)
        
           
        if not from_.bot and 'cuan' in pesan or 'Cuan' in pesan:
            print(time.asctime(), pesan)
            await bentar(2)
            await event.reply('0pay *')
            return
           
            
        
    client.start() 
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')
	
	