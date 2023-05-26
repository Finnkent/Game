#!/usr/bin/env python3
import time, asyncio, sys


from telethon import TelegramClient, events, utils, Button

api_id = 18850178 
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = input("Mau akun mana = ")

Casino = '/masak_MiniBacon_220'
bot_id = 'kampungmaifambot'
ch = ''
tunggu = 3420
ternak = '/beliternak_Ayam_Piqucum'

with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(bot_id, Casino))

    @client.on(events.NewMessage(from_users=bot_id))
    async def handler(event):
        pesan = event.raw_text
        
        if "Berhasil memasak" in pesan:
            time.sleep(2)
            await event.respond(Casino)
            print(pesan)
            return
        
        elif "Tidak cukup bahan" in pesan:
            print(pesan)
            return
          
        elif "Kamu tidak memiliki" in pesan:
            time.sleep(2)
            await event.respond('/restore')
            print(pesan)
            return
        
        elif "Energi berhasil" in pesan:
            time.sleep(2)
            await event.respond(Casino)
            print(pesan)
            return
        
        elif "Kamu tidak bisa memasak" in pesan:
            time.sleep(2)
            await event.respond('/levelupGuild')
            print(time.asctime(), 'Level up')
            return
          
        #elif "Guildmu sekarang adalah" in pesan:
            #time.sleep(2)
            #await client.forward_messages(ch, event.message)
            #time.sleep(tunggu)
            #await event.respond(Casino)
            #return
          
        elif "EXP tidak mencukupi" in pesan:
            print(time.asctime(), 'EXP gak cukup')
            time.sleep(tunggu)
            await event.respond(Casino)
            return
                
        elif "Hanya ketua atau wakil ketua guild yang bisa mengupgrade guild" in pesan:
            print(time.asctime(), 'Lu gabisa upgrade guild')
            time.sleep(tunggu)
            await event.respond(Casino)
            return
                
    client.start() 
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')
	
	