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
'MentimunA',
'Tomat',
'TomatE',
'TomatD',
'TomatC',
'TomatB',
'TomatA',
'Cabai',
'CabaiE',
'CabaiD',
'CabaiC',
'CabaiB',
'CabaiA',
'Wortel',
'WortelE',
'WortelD',
'WortelC',
'WortelB',
'WortelA',
'Kentang',
'KentangE',
'KentangD',
'KentangC',
'KentangB',
'KentangA',
'Avokad',
'AvokadE',
'AvokadD',
'AvokadC',
'AvokadB',
'AvokadA',
'Apel',
'ApelE',
'ApelD',
'ApelC',
'ApelB',
'ApelA',
'Pisang',
'PisangE',
'PisangD',
'PisangC',
'PisangB',
'PisangA',
'Jagung',
'JagungE',
'JagungD',
'JagungC',
'JagungB',
'JagungA',
'NanasKeramat',
'NanasKeramatE',
'NanasKeramatD',
'NanasKeramatC',
'NanasKeramatB',
'NanasKeramatA',
'Strawberry',
'StrawberryE',
'StrawberryD',
'StrawberryC',
'StrawberryB',
'StrawberryA',
'Anggur',
'AnggurE',
'AnggurD',
'AnggurC',
'AnggurB',
'AnggurA',
'Lily',
'LilyE',
'LilyD',
'LilyC',
'LilyB',
'LilyA',
'Jeruk',
'JerukE',
'JerukD',
'JerukC',
'JerukB',
'JerukA',
'Nanas',
'NanasE',
'NanasD',
'NanasC',
'NanasB',
'NanasA',
'Semangka',
'SemangkaE',
'SemangkaD',
'SemangkaC',
'SemangkaB',
'SemangkaA',
'BungaMatahari',
'BungaMatahariE',
'BungaMatahariD',
'BungaMatahariC',
'BungaMatahariB',
'BungaMatahariA',
'Sakura',
'SakuraE',
'SakuraD',
'SakuraC',
'SakuraB',
'SakuraA',
'Melon',
'MelonE',
'MelonD',
'MelonC',
'MelonB',
'MelonA',
'Pepaya',
'PepayaE',
'PepayaD',
'PepayaC',
'PepayaB',
'PepayaA',
'Jambu',
'JambuE',
'JambuD',
'JambuC',
'JambuB',
'JambuA',
'Nangka',
'NangkaE',
'NangkaD',
'NangkaC',
'NangkaB',
'NangkaA',
'Terung',
'TerungE',
'TerungD',
'TerungC',
'TerungB',
'TerungA',
'Kelapa',
'KelapaE',
'KelapaD',
'KelapaC',
'KelapaB',
'KelapaA',
'Ubi',
'UbiE',
'UbiD',
'UbiC',
'UbiB',
'UbiA',
'Tulip',
'TulipE',
'TulipD',
'TulipC',
'TulipB',
'TulipA',
'Mawar',
'MawarE',
'MawarD',
'MawarC',
'MawarB',
'MawarA',
'Pir',
'PirE',
'PirD',
'PirC',
'PirB',
'PirA',
'Rambutan',
'RambutanE',
'RambutanD',
'RambutanC',
'RambutanB',
'RambutanA',
'KacangTanah',
'KacangTanahE',
'KacangTanahD',
'KacangTanahC',
'KacangTanahB',
'KacangTanahA',
'Mangga',
'ManggaE',
'ManggaD',
'ManggaC',
'ManggaB',
'ManggaA',
'TerungKeramat',
'TerungKeramatE',
'TerungKeramatD',
'TerungKeramatC',
'TerungKeramatB',
'TerungKeramatA',
'ManggaKeramat',
'ManggaKeramatE',
'ManggaKeramatD',
'ManggaKeramatC',
'ManggaKeramatB',
'ManggaKeramatA',
'BuahNaga',
'BuahNagaE',
'BuahNagaD',
'BuahNagaC',
'BuahNagaB',
'BuahNagaA',
'Persik',
'PersikE',
'PersikD',
'PersikC',
'PersikB',
'PersikA',
'BerryKeramat',
'BerryKeramatE',
'BerryKeramatD',
'BerryKeramatC',
'BerryKeramatB',
'BerryKeramatA',
'AnggurKeramat',
'AnggurKeramatE',
'AnggurKeramatD',
'AnggurKeramatC',
'AnggurKeramatB',
'AnggurKeramatA',
'PisangKeramat',
'PisangKeramatE',
'PisangKeramatD',
'PisangKeramatC',
'PisangKeramatB',
'PisangKeramatA',
'TomatKeramat',
'TomatKeramatE',
'TomatKeramatD',
'TomatKeramatC',
'TomatKeramatB',
'TomatKeramatA',
'WortelKeramat',
'WortelKeramatE',
'WortelKeramatD',
'WortelKeramatC',
'WortelKeramatB',
'WortelKeramatA',
'LabuKeramat',
'LabuKeramatE',
'LabuKeramatD',
'LabuKeramatC',
'LabuKeramatB',
'LabuKeramatA',
]



hasil = "/casino_hasil"
judi = "/casino_LuckyTen_"

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
            
            
        if "dimiliki:" in message:
            idMer = event.id
            msg = await client.get_messages(bot[1],ids = idMer)
            time.sleep(1.5)
            a = event.raw_text
            b = a.split()
            c = b.index('dimiliki:')
            d = b[c+1]
            if int(d) < 500:
                await msg.click(text="Gabung 15")
                return
            elif int(d) <= 500 or int(d) < 1000:
                await msg.click(text="Gabung 500")
                return
            elif int(d) <= 1000 or int(d) < 1500:
                await msg.click(text="Gabung 1000")
                return
            elif int(d) >= 1500:
                await msg.click(text="Gabung 1500")
            return
                    
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
                await client.send_message(bot[3], judi+str(random.randint(1,2))+"_25e10")
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
        
            if merge %246 == 0 :
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
    print(time.asctime(), '-', 'Mari menjadi petani')
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Istirahat dulu capek')
