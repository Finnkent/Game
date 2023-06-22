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

mergeList = [
'Mentimun',
'Anggur',
'Apel',
'Avokad',
'BungaMatahari',
'Cabai',
'Jagung',
'Jeruk',
'Kentang',
'Lily',
'Mawar',
'Melon',
'Mentimun',
'Nanas',
'Pisang',
'Sakura',
'Semangka',
'Strawberry',
'Tomat',
'Wortel',
'BuahNaga',
'Jambu',
'KacangTanah',
'Kelapa',
'Mangga',
'Nangka',
'Pepaya',
'Persik',
'Pir',
'Rambutan',
'Terung',
'Tulip',
'Ubi',
'AnggurKeramat',
'BerryKeramat',
'LabuKeramat',
'ManggaKeramat',
'NanasKeramat',
'PisangKeramat',
'TerungKeramat',
'TomatKeramat',
'WortelKeramat',
'Last',
]

Grade = [
'',
'E',
'D',
'C',
'B',
'A',
'Last',
]

hasil = "/casino_hasil"
judi = "/casino_FiftyFifty_"
ternak = "/ambilHasil"
makan = "/beriMakan"
mese = '/sg_harvest'
bot = ['danaudalamhutan', 'KampungMaifamXBot', 'KampungMaifamX4Bot', 'KampungMaifamBot']
turu = 4
mer = 0
gradenum = 0
panen = '/sg_panen'

async def bentar(w):
    await asyncio.sleep(w)

with TelegramClient(sesi_fil, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(bot[1], panen))
    @client.on(events.NewMessage(incoming=True, from_users=bot[1]))
    async def handler(event):
        pesan = event.raw_text
        global mer
        global idMer
        global gradenum
            
        if "di keranjang buah" in pesan:
            mer += 1
            time.sleep(2)
            await event.respond('/sg_merge_'+mergeList[mer]+Grade[gradenum])
            return
            
        if "Kamu tidak memiliki" in pesan:
            mer +=1
            
            if mer %15 == 0 :
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
                
            await bentar(0.9)
            await event.respond('/sg_merge_'+mergeList[mer]+Grade[gradenum])
            return

        if 'cukup energi' in pesan:
            time.sleep(2)
            await event.respond('/restore_max_confirm')
            return

        if 'Keranjang buah tidak mencukupi' in pesan:
            time.sleep(2)
            await event.respond('/sg_merge_'+mergeList[mer]+Grade[gradenum])
            return
            
        if 'Berhasil memanen' in pesan:
            time.sleep(2)
            await event.respond(mese)
            return

        if 'Tidak ada yang bisa' in pesan:
            #print('masuk')
            time.sleep(2)
            await event.respond('/sg_merge_'+mergeList[mer]+Grade[gradenum])
            return

        if 'untuk mendapat' in pesan:
            idMer = event.id
            msg = await client.get_messages(bot[1],ids = idMer)
            time.sleep(1.5)
            a = event.raw_text
            b = a.split()
            c = b.index('dimiliki:')
            d = b[c+1]
            if int(d) <= 5 or int(d) < 10:
                await msg.click(text="Gabung 5")
                return
            elif int(d) <= 10 or int(d) < 15:
                await msg.click(text="Gabung 10")
                return
            elif int(d) <= 15 or int(d) < 500:
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


        if 'Berhasil menggabungkan' in pesan:
            idMer = event.id
            await bentar(0.9)
            await event.respond('/sg_merge_'+mergeList[mer]+Grade[gradenum])
            return
          
              
        if mergeList[mer] == mergeList[-1]:
            gradenum +=1
            mer = 0
            print('Yosh Naik Grade!!')
            time.sleep(2)
            await event.respond('/sg_merge_'+mergeList[mer]+Grade[gradenum])
            return
            
        if Grade[gradenum] == Grade[-1]:
            gradenum = 0
            mer = 0
            print('Yosh Ulang!!')
            time.sleep(2)
            await event.respond(mese)
            return

    client.start()
    print(time.asctime(), '-', 'Mari menjadi petani')
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Istirahat dulu capek')

