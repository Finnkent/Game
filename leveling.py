#!/usr/bin/env python3
import time, asyncio, sys


from telethon import TelegramClient, events, utils

api_id = 18850178 
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = input('Mau akun mana = ')

Leveling = '/tanamGuild_Wortel_1000'
Beli = '/beli_Wortel_1e6'
#Panen = '/KebunGuild_AmbilPanen'
Panen = '/kebunGuild_PanenSekarang'
Siram = '/KebunGuild_Siram'
    
with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('KampungMaifamBot', Leveling))

    @client.on(events.NewMessage(from_users='KampungMaifamBot'))
    async def handler(event):
        pesan = event.raw_text
        
        if 'Sekarang kamu menjadi petani level 118' in pesan:
            time.sleep(2)
            print('--Selesai--')
            exit
            
        elif 'Kamu berhasil menanam' in pesan:
            print(time.asctime(), 'Berhasil menanam')
            time.sleep(2)
            await event.respond(Panen)
            #await event.respond(Siram)
            return
          
        elif 'Berhasil menyiram tanaman' in pesan:
            print(time.asctime(), 'Berhasil menyiram')
            #time.sleep(2)
            time.sleep(182)
            await event.respond(Panen)
            return
        
        elif 'Berhasil memanen' in pesan:
            print(time.asctime(), 'Berhasil memanen')
            time.sleep(2)
            await event.respond('/levelup')
            return
        
        elif 'EXP kamu tidak mencukupi' in event.raw_text or 'Sekarang kamu menjadi' in pesan:
            print(pesan)
            time.sleep(2)
            await event.respond(Leveling)
            return
        
        elif 'Lahan tersisa di kebun' in pesan:
            print(time.asctime(), 'Lahan gak cukup')
            time.sleep(2)
            await event.respond(Panen)
            return
        
        elif 'Tidak ada yang bisa' in pesan:
            print(time.asctime(), 'Gabisa panen')
            time.sleep(2)
            await event.respond(Leveling)
            return
        
        elif 'untuk ditanam' in pesan:
            print(time.asctime(), 'Habis bibit')
            time.sleep(2)
            await event.respond(Beli)
            return
          
        elif 'Kamu tidak memiliki cukup energi' in pesan:
            print(time.asctime(), 'Habis energi')
            time.sleep(2)
            await event.respond('/restore')
            return
        
        elif 'Energi berhasil' in pesan:
            print(time.asctime(), 'Energi pulih')
            time.sleep(2)
            await event.respond(Leveling)
            return
        
        elif 'Berhasil membeli' in pesan:
            print(time.asctime(), 'Bibit berhasil di beli')
            time.sleep(2)
            await event.respond(Leveling)
            return
         
        
        
    client.start() 
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')
	
	