#by Adtz
import time
import asyncio
import threading
#import sys, re
#import random
from telethon import TelegramClient, events

bot_id = 'KampungMaifamBot'
api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'

mine = "/spex"

loop = asyncio.new_event_loop()

client = TelegramClient("04", api_id, api_hash)
client2 = TelegramClient("05", api_id, api_hash)
client3 = TelegramClient("06", api_id, api_hash)
client4 = TelegramClient("07", api_id, api_hash)
client5 = TelegramClient("08", api_id, api_hash)
client6 = TelegramClient("09", api_id, api_hash)
client7 = TelegramClient("10", api_id, api_hash)
client8 = TelegramClient("11", api_id, api_hash)

all = ["04", "05", "06", "07", "08", "09", "10", "11"]

for i in all:
    print(time.asctime(), '-', str(i)+' Gas space')
    #time.sleep()
    
async def script(event): #masukin script di sini
    pesan = event.raw_text
    
    if "Collect as" in pesan or "Kumpulkan mineral" in pesan:
        time.sleep(172)
        await event.click(text = "⛏")
        print(time.asctime(), "Dapat batuan")
        
    if "Good Job!!" in pesan or "Kerja Bagus!!" in pesan:
        time.sleep(2.5)
        await event.respond("/spex_WRD2023")
    
    if "WorldRockDay2023" in pesan:
        time.sleep(2.5)
        await event.respond("/restore")
    
    if "restored" in pesan or "berhasil dipulihkan" in pesan:
        time.sleep(2.5)
        await event.respond(mine)
        
        
@client.on(events.NewMessage(from_users=bot_id))
async def my_event_handler(event):
    await script(event)
client.start()

@client2.on(events.NewMessage(from_users=bot_id))
async def my_event_handler(event):
    await script(event)
client2.start()

@client3.on(events.NewMessage(from_users=bot_id))
async def my_event_handler(event):
    await script(event)
client3.start()

@client4.on(events.NewMessage(from_users=bot_id))
async def my_event_handler(event):
    await script(event)
client4.start()

@client5.on(events.NewMessage(from_users=bot_id))
async def my_event_handler(event):
    await script(event)
client5.start()

@client6.on(events.NewMessage(from_users=bot_id))
async def my_event_handler(event):
    await script(event)
client6.start()

@client7.on(events.NewMessage(from_users=bot_id))
async def my_event_handler(event):
    await script(event)
client7.start()

@client8.on(events.NewMessage(from_users=bot_id))
async def my_event_handler(event):
    await script(event)
client8.start()


client.loop.run_forever()