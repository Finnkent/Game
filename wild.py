#!/usr/bin/env python3
import time, asyncio, sys


from telethon import TelegramClient, events, utils, Button

api_id = 18850178 
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = input("Mau akun mana = ")

dest = 'KampungMaifamXBot'
Ternak = '/pelihara_BayiRusa_127'
#restore = '/restore'
restore = '/restore_max_confirm'
 
with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(dest, Ternak))

    @client.on(events.NewMessage(from_users='KampungMaifamXBot'))
    async def handler(event):
        pesan = event.raw_text
        
        if "Berhasil menambahkan" in pesan or "Kandang ternak khusus penuh" in pesan:
            print(time.asctime(), 'Isi kandang')
            time.sleep(2)
            await event.respond('/ambilHewan')
            return
        
        if "Kamu berhasil mendapat" in pesan:
            print(time.asctime(), 'Ambil hasil')
            time.sleep(2)
            await event.respond(Ternak)
            #await event.respond('/act_WildBreeder')
            return
          
        #if "WildBreeder" in pesan:
            #time.sleep(2)
            #print(pesan)
            #await event.click(text="Claim")
            #await event.respond(Ternak)
            #return
        
        if "Kamu tidak memiliki cukup energi" in pesan:
            print('Energi habis')
            time.sleep(2)
            await event.respond(restore)
            print(time.asctime(), 'Isi Ulang Energi')
            return
                
        if "Energi berhasil" in pesan:
            print(time.asctime(), 'Energi pulih')
            time.sleep(2)
            await event.respond(Ternak) 
            return
        
        
    client.start() 
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')
	
	