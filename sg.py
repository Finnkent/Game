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
sesi_fil = 'Finnkent'

bot = ['danaudalamhutan', 'KampungMaifamXBot', 'KampungMaifamX4Bot', 'KampungMaifamBot']

plant = [
'Mentimun',
'MentimunE',
'MentimunD',
'MentimunC',
'MentimunB',
'Tomat',
'TomatE',
'TomatD',
'TomatC',
'TomatB',
'Cabai',
'CabaiE',
'CabaiD',
'CabaiC',
'CabaiB',
'Wortel',
'WortelE',
'WortelD',
'WortelC',
'WortelB',
'Kentang',
'KentangE',
'KentangD',
'KentangC',
'KentangB',
'Avokad',
'AvokadE',
'AvokadD',
'AvokadC',
'AvokadB',
'Apel',
'ApelE',
'ApelD',
'ApelC',
'ApelB',
'Pisang',
'PisangE',
'PisangD',
'PisangC',
'PisangB',
'Jagung',
'JagungE',
'JagungD',
'JagungC',
'JagungB',
'NanasKeramat',
'NanasKeramatE',
'NanasKeramatD',
'NanasKeramatC',
'NanasKeramatB',
'Strawberry',
'StrawberryE',
'StrawberryD',
'StrawberryC',
'StrawberryB',
'Anggur',
'AnggurE',
'AnggurD',
'AnggurC',
'AnggurB',
'Lily',
'LilyE',
'LilyD',
'LilyC',
'LilyB',
'Jeruk',
'JerukE',
'JerukD',
'JerukC',
'JerukB',
'Nanas',
'NanasE',
'NanasD',
'NanasC',
'NanasB',
'Semangka',
'SemangkaE',
'SemangkaD',
'SemangkaC',
'SemangkaB',
'BungaMatahari',
'BungaMatahariE',
'BungaMatahariD',
'BungaMatahariC',
'BungaMatahariB',
'Sakura',
'SakuraE',
'SakuraD',
'SakuraC',
'SakuraB',
'Melon',
'MelonE',
'MelonD',
'MelonC',
'MelonB',
'Pepaya',
'PepayaE',
'PepayaD',
'PepayaC',
'PepayaB',
'Jambu',
'JambuE',
'JambuD',
'JambuC',
'JambuB',
'Nangka',
'NangkaE',
'NangkaD',
'NangkaC',
'NangkaB',
'Terung',
'TerungE',
'TerungD',
'TerungC',
'TerungB',
'Kelapa',
'KelapaE',
'KelapaD',
'KelapaC',
'KelapaB',
'Ubi',
'UbiE',
'UbiD',
'UbiC',
'UbiB',
'Tulip',
'TulipE',
'TulipD',
'TulipC',
'TulipB',
'Mawar',
'MawarE',
'MawarD',
'MawarC',
'MawarB',
'Pir',
'PirE',
'PirD',
'PirC',
'PirB',
'Rambutan',
'RambutanE',
'RambutanD',
'RambutanC',
'RambutanB',
'KacangTanah',
'KacangTanahE',
'KacangTanahD',
'KacangTanahC',
'KacangTanahB',
'Mangga',
'ManggaE',
'ManggaD',
'ManggaC',
'ManggaB',
'TerungKeramat',
'TerungKeramatE',
'TerungKeramatD',
'TerungKeramatC',
'TerungKeramatB',
'ManggaKeramat',
'ManggaKeramatE',
'ManggaKeramatD',
'ManggaKeramatC',
'ManggaKeramatB',
'BuahNaga',
'BuahNagaE',
'BuahNagaD',
'BuahNagaC',
'BuahNagaB',
'Persik',
'PersikE',
'PersikD',
'PersikC',
'PersikB',
'BerryKeramat',
'BerryKeramatE',
'BerryKeramatD',
'BerryKeramatC',
'BerryKeramatB',
'AnggurKeramat',
'AnggurKeramatE',
'AnggurKeramatD',
'AnggurKeramatC',
'AnggurKeramatB',
'PisangKeramat',
'PisangKeramatE',
'PisangKeramatD',
'PisangKeramatC',
'PisangKeramatB',
'TomatKeramat',
'TomatKeramatE',
'TomatKeramatD',
'TomatKeramatC',
'TomatKeramatB',
'WortelKeramat',
'WortelKeramatE',
'WortelKeramatD',
'WortelKeramatC',
'WortelKeramatB',
'LabuKeramat',
'LabuKeramatE',
'LabuKeramatD',
'LabuKeramatC',
'LabuKeramatB',
]



hasil = "/casino_hasil"
judi = "/casino_FiftyFifty_"

ternak = "/ambilHasil"
makan = "/beriMakan"

gas = "/sg_gabung_mentimun"
turu = 4
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
            
            
        if "Gabungkan 1000" in message:
            idMer = event.id
            await bentar(0.9)
            await event.click(text='Gabung 500')
        
        elif "untuk mendapat" in message:
            idMer = event.id
            await bentar(0.9)
            await event.click(text='Gabung 15')
                    
        if "Berhasil menggabungkan" in message:
            await bentar(0.9)
            msg = await client.get_messages(bot[1],ids = idMer)
            await msg.click(0,2)
            return
          
        
        if "Kamu tidak memiliki" in message:
            merge +=1
            await bentar(turu)
            
            if merge %15 == 0 :
                await client.send_message(bot[3], hasil)
                await bentar(turu)
                await client.send_message(bot[3], judi+str(random.randint(1,2))+"_1e12")
                await bentar(turu)
                await client.send_message(bot[3], ternak)
                await bentar(turu)
                await client.send_message(bot[3], makan)
                await bentar(turu)
                await client.send_message(bot[3], "/pfs_AreaClassE_ambilpanen")
                await bentar(turu)
                await client.send_message(bot[3], "/pfs_AreaClassD_ambilpanen")
                await bentar(turu)
                await client.send_message(bot[3], "/pfs_AreaClassC_ambilpanen")
                await bentar(turu)
                await client.send_message(bot[3], "/pfs_AreaClassS_ambilpanen")
                await bentar(turu)
                await client.send_message(bot[3], "/sg_panen")
                await bentar(10)
        
            if merge %205 == 0 :
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
           
            
        #if "Keranjang buah tidak mencukupi" in message:
            #await bentar(5)
            #await client.send_message(bot[3], "/sg_kirimPanen")
          
        #if "KeranjangBuah 🧺 SkyGarden" in message:
            #time.sleep(2)
            
        
            
    client.start()
    print(time.asctime(), '-', 'Mari menjadi petani')
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Istirahat dulu capek')
