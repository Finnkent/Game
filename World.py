import time
import asyncio
import sys

from telethon import TelegramClient, events, utils

api_id = 18850178 
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = input("Mau akun mana = ")
loop = asyncio.new_event_loop()

space = '/wo2023_KumpulkanSampah'
    
with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('KampungMaifamX4Bot', space))

    @client.on(events.NewMessage(from_users='KampungMaifamX4Bot'))
    async def handler(event):
    	
        if "Lepaskan alat yang" in event.raw_text:
            Doo = await client.get_messages('KampungMaifamX4Bot', ids=event.message.id)
            time.sleep(31)
            await Doo.click(text='KumpulkanSampah')        
            return
        
        if "Kamu mencari sampah menggunakan Jala" in event.raw_text:
            Doo = await client.get_messages('KampungMaifamX4Bot', ids=event.message.id)
            time.sleep(33.1)
            await Doo.click(text='KumpulkanSampah')        
            return
          
        if "Kamu mencari sampah menggunakan Pancing" in event.raw_text:
            Doo = await client.get_messages('KampungMaifamX4Bot', ids=event.message.id)
            time.sleep(16.1)
            await Doo.click(text='KumpulkanSampah')        
            return
          
        if "Kamu mencari sampah menggunakan Tongkat" in event.raw_text:
            Doo = await client.get_messages('KampungMaifamX4Bot', ids=event.message.id)
            time.sleep(5.1)
            await Doo.click(text='KumpulkanSampah')        
            return
            
        if "Energi tidak" in event.raw_text:
            Doo = await client.get_messages('KampungMaifamX4Bot', ids=event.message.id)
            time.sleep(2)
            await event.respond('/wo2023_restore')        
            return
            
        if "Kamu meminum" in event.raw_text:
            time.sleep(2)
            await event.respond(space)        
            return
            
        if "Tunggu setidaknya" in event.raw_text:
            Doo = await client.get_messages('KampungMaifamX4Bot', ids=event.message.id)
            time.sleep(31)
            await Doo.click(text='KumpulkanSampah')        
            return
           
        
            
    client.start()
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Berhenti')