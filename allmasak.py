from telethon import TelegramClient, events, sync, utils
from time import sleep
import asyncio, random

loop = asyncio.get_event_loop()

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'

akun1 = "04"
akun2 = "05"
akun3 = "06"
akun4 = "07"
akun5 = "08"
akun6 = "09"
client = TelegramClient(akun1, api_id, api_hash).start()
client2 = TelegramClient(akun2, api_id, api_hash).start()
client3 = TelegramClient(akun3, api_id, api_hash).start()
client4 = TelegramClient(akun4, api_id, api_hash).start()
client5 = TelegramClient(akun5, api_id, api_hash).start()
client6 = TelegramClient(akun6, api_id, api_hash).start()

chat = 'kampungmaifambot'
Masak = '/masak_MiniBacon_220'

@client.on(events.NewMessage(chat))
async def handler(event):
    
    if "Berhasil memasak" in event.text:
        sleep(3)
        await event.respond(Masak)
        print(pesan)
        return
        
    elif "Kamu tidak bisa memasak" in event.text:
        print(time.asctime(), 'istirahat dulu')
        sleep(3500)
        await event.respond(Masak)
        return
 
          
    elif 'Kamu tidak memiliki' in event.text:
        sleep(3)
        await event.respond('/restore')
        return
                
    elif 'Energi berhasil' in event.text:
        sleep(3)
        await event.respond(Masak)
        return
        
       
@client2.on(events.NewMessage(chat))
async def handler(event):
    
    if "Berhasil memasak" in event.text:
        sleep(3)
        await event.respond(Masak)
        return
        
    elif "Kamu tidak bisa memasak" in event.text:
        print(time.asctime(), 'istirahat dulu')
        sleep(3500)
        await event.respond(Masak)
        return
 
          
    elif 'Kamu tidak memiliki' in event.text:
        sleep(3)
        await event.respond('/restore')
        return
                
    elif 'Energi berhasil' in event.text:
        sleep(3)
        await event.respond(Masak)
        return
        
    
@client3.on(events.NewMessage(chat))
async def handler(event):
    
    if "Berhasil memasak" in event.text:
        sleep(3)
        await event.respond(Masak)
        return
        
    elif "Kamu tidak bisa memasak" in event.text:
        print(time.asctime(), 'istirahat dulu')
        sleep(3500)
        await event.respond(Masak)
        return
 
          
    elif 'Kamu tidak memiliki' in event.text:
        sleep(3)
        await event.respond('/restore')
        return
                
    elif 'Energi berhasil' in event.text:
        sleep(3)
        await event.respond(Masak)
        return
        
    
@client4.on(events.NewMessage(chat))
async def handler(event):
    
    if "Berhasil memasak" in event.text:
        sleep(3)
        await event.respond(Masak)
        return
        
    elif "Kamu tidak bisa memasak" in event.text:
        print(time.asctime(), 'istirahat dulu')
        sleep(3500)
        await event.respond(Masak)
        return
 
          
    elif 'Kamu tidak memiliki' in event.text:
        sleep(3)
        await event.respond('/restore')
        return
                
    elif 'Energi berhasil' in event.text:
        sleep(3)
        await event.respond(Masak)
        return
        
    
@client5.on(events.NewMessage(chat))
async def handler(event):
    
    if "Berhasil memasak" in event.text:
        sleep(3)
        await event.respond(Masak)
        return
        
    elif "Kamu tidak bisa memasak" in event.text:
        print(time.asctime(), 'istirahat dulu')
        sleep(3500)
        await event.respond(Masak)
        return
 
          
    elif 'Kamu tidak memiliki' in event.text:
        sleep(3)
        await event.respond('/restore')
        return
                
    elif 'Energi berhasil' in event.text:
        sleep(3)
        await event.respond(Masak)
        return
        
    
@client6.on(events.NewMessage(chat))
async def handler(event):
    
    if "Berhasil memasak" in event.text:
        sleep(3)
        await event.respond(Masak)
        return
        
    elif "Kamu tidak bisa memasak" in event.text:
        print(time.asctime(), 'istirahat dulu')
        sleep(3500)
        await event.respond(Masak)
        return
 
          
    elif 'Kamu tidak memiliki' in event.text:
        sleep(3)
        await event.respond('/restore')
        return
                
    elif 'Energi berhasil' in event.text:
        sleep(3)
        await event.respond(Masak)
        return
        
    

                
client.run_until_disconnected()
client2.run_until_disconnected()
client3.run_until_disconnected()
client4.run_until_disconnected()
client5.run_until_disconnected()
client6.run_until_disconnected()