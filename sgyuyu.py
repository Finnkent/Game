import time, os
import asyncio
import sys, re
import random
from time import sleep
from random import randint
from datetime import datetime
from telethon import TelegramClient, events, utils, Button
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_fil = 'Yuyu'

bot = ['danaudalamhutan', 'KampungMaifamXBot', 'KampungMaifamX4Bot', 'KampungMaifamBot']

plant = [
'Mentimun',
'MentimunE',
'Tomat',
'TomatE',
'Cabai',
'CabaiE',
'Wortel',
'WortelE',
'Kentang',
'KentangE',
'Avokad',
'AvokadE',
'Apel',
'ApelE',
'Pisang',
'PisangE',
'Jagung',
'JagungE',
'NanasKeramat',
'NanasKeramatE',
'Strawberry',
'StrawberryE',
'Anggur',
'AnggurE',
'Lily',
'LilyE',
'Jeruk',
'JerukE',
'Nanas',
'NanasE',
'Semangka',
'SemangkaE',
'BungaMatahari',
'BungaMatahariE',
'Sakura',
'SakuraE',
'Melon',
'MelonE',
'Pepaya',
'PepayaE',
'Jambu',
'JambuE',
'Nangka',
'NangkaE',
'Terung',
'TerungE',
'Kelapa',
'KelapaE',
'Ubi',
'UbiE',
'Tulip',
'TulipE',
'Mawar',
'MawarE',
'Pir',
'PirE',
'Rambutan',
'RambutanE',
'KacangTanah',
'KacangTanahE',
'Mangga',
'ManggaE',
'TerungKeramat',
'TerungKeramatE',
'ManggaKeramat',
'ManggaKeramatE',
'BuahNaga',
'BuahNagaE',
'Persik',
'PersikE',
'BerryKeramat',
'BerryKeramatE',
'AnggurKeramat',
'AnggurKeramatE',
'PisangKeramat',
'PisangKeramatE',
'TomatKeramat',
'TomatKeramatE',
'WortelKeramat',
'WortelKeramatE',
'LabuKeramat',
'LabuKeramatE',
]

hasil = "/casino_hasil"
judi = "/casino_LuckyTen_"

ternak = "/ambilHasil"
makan = "/beriMakan"

gas = "/sg_gabung_mentimun"

turu = 3
merge = 0

async def bentar(w):
    await asyncio.sleep(w)
    
with TelegramClient(sesi_fil, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(bot[1], gas))
    @client.on(events.NewMessage(incoming=True, from_users=bot[1]))
    async def handle_chat(event):
        message = event.raw_text
        global merge
        global idMer
            
        if "Gabungkan 500" in message:
            idMer = event.id
            await bentar(0.9)
            await event.click(text='Gabung 500')
        
        elif "untuk mendapat" in message:
            idMer = event.id
            await bentar(0.9)
            await event.click(text='Gabung 5')
                    
        if "Berhasil menggabungkan" in message:
            await bentar(0.9)
            msg = await client.get_messages(bot[1],ids = idMer)
            await msg.click(0,0)
            return
          
        if "Kamu tidak memiliki" in message:
            merge +=1
            await bentar(turu)
            
            if merge %5 == 0 :
                await client.send_message(bot[3], hasil)
                await bentar(turu)
                await client.send_message(bot[3], judi+str(random.randint(1,2))+"_25e10")
                await bentar(turu)
                await client.send_message(bot[3], ternak)
                await bentar(turu)
                await client.send_message(bot[3], makan)
                await bentar(turu)
                await client.send_message(bot[3], "/pfs_AreaClassA_ambilpanen")
                await bentar(turu)
                await client.send_message(bot[3], "/pfs_AreaClassS_ambilpanen")
                await bentar(turu)
                await client.send_message(bot[3], "/masak_MiniBacon_220")
                await bentar(turu)
                await client.send_message(bot[3], "/sg_panen")
                await bentar(10)
        
            if merge %41 == 0 :
                await bentar(turu)
                print(time.asctime(), ' Furnace & seedMaker')
                for furnace in range(1,11):
                    ironbar = '/furnace_'+str(furnace)+'_add_confirm'
                    await client.send_message(bot[2], ironbar)
                    time.sleep(5)
                    await client.send_message(bot[2], ironbar)
                    time.sleep(5)
                    sleep(5)
                        
                for bibit in range(1,2):
                    seed = '/seedmaker_'+str(bibit)+'_AnggurKeramatS_confirm'
                    await client.send_message(bot[2], seed)
                    time.sleep(5)
                    await client.send_message(bot[2], seed)
                    time.sleep(5)
                    sleep(5)
                await bentar(turu)
            await client.send_message(bot[1], "/sg_gabung_"+str(plant[merge]))
        
        list = len(plant)
        if merge == (list-1):
            await bentar(turu)
            await client.send_message(bot[3], "/sg_panen")
            
            merge=0

    @client.on(events.NewMessage(from_users=bot[3]))
    async def handle_chat(event):
        message = event.raw_text
        
        if "Kamu tidak memiliki cukup energi" in message:
            print(time.asctime(), 'Capek aseli')
            await bentar(2)
            await client.send_message(bot[3], "/makan_RotiBelanda")
            
        if "Tidak tidak" in message:
            print(time.asctime(), 'Kenyang WOI!!!')
            await bentar(2)
            await client.send_message(bot[3], "/restore_max_confirm")
            


    client.start()
    print(time.asctime(), '-', 'Mari nguli')
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Istirahat dulu capek')
