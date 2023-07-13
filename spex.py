import time, asyncio, sys, random

from telethon import TelegramClient, events, utils, Button

api_id = 18850178 
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = input('Akun = ')

space = 'SpaceExploration'
restore = '/restore'
bot = 'KampungMaifamX4Bot'

with TelegramClient(sesi_file, api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message(bot, space))
        
        @client.on(events.NewMessage(from_users=bot))
        async def handler(event):
            
            if 'Kumpulkan mineral sebanyak' in event.raw_text:
                time.sleep(300)
                await event.click(text="⛏")
                return

            if 'Proses tambang berlangsung' in event.raw_text:
                time.sleep(2)
                print(event.raw_text)
                await event.respond('/restore')
                return

            if 'Kamu tidak memiliki cukup' in event.raw_text:
                time.sleep(2)
                await event.respond('/restore')
                return

            if 'Energi berhasil dipulihkan' in event.raw_text:
                time.sleep(2)
                await event.respond(space)
                return


        client.start() 
        client.run_until_disconnected() 
        print(time.asctime(), '-', 'berhenti')
	
