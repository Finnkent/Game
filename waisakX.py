import time
import asyncio
import sys
from telethon import TelegramClient, events, utils

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_fil = input("Mau akun mana = ")

pesan = '/waisak2567BE_MisiTambang'

mine1 = '/waisak2567BE_GuaTambang_1'
mine2 = '/waisak2567BE_GuaTambang_2'
mine3 = '/waisak2567BE_GuaTambang_3'
mine4 = '/waisak2567BE_GuaTambang_4'
mine5 = '/waisak2567BE_GuaTambang_5'
mine6 = '/waisak2567BE_GuaTambang_6'
mine7 = '/waisak2567BE_GuaTambang_7'
mine8 = '/waisak2567BE_GuaTambang_8'
mine9 = '/waisak2567BE_GuaTambang_9'
mine10 = '/waisak2567BE_GuaTambang_10'
mine11 = '/waisak2567BE_GuaTambang_1'
mine12 = '/waisak2567BE_GuaTambang_2'
mine13 = '/waisak2567BE_GuaTambang_3'
mine14 = '/waisak2567BE_GuaTambang_4'
mine15 = '/waisak2567BE_GuaTambang_5'
mine16 = '/waisak2567BE_GuaTambang_6'
mine17 = '/waisak2567BE_GuaTambang_7'
mine18 = '/waisak2567BE_GuaTambang_8'

lt1 = ['◻️Kalifornium545[S]', '◼️BlackDiamond[S]', '◻️Kalifornium545[B]', '◻️Magistone[B]', '◻️Kalifornium565[C]', '💀FosilNaga[B]', '◻️Kalifornium525[C]', '💀FosilTRex[B]', '🔷RedDiamond[B]', '▪️Batu[C]', '🔹Iridium[B]', '🔶Poudretteite[A]', '🔶RedBeryl[A]', '▪️BijihBesi[C]', '💀FosilAlien[C]', '🔹Iridium', '🔶Musgravite[C]', '🔸Emas[C]', '💀FosilTriceratops', '💀FosilNaga', '💀FosilTRex[E]', '◻️Magistone[E]', '💀FosilNaga[D]', '💀FosilAlien[D]', '🔷Serendibite[D]', '🔶Musgravite[D]', '🔶FireOpal[D]', '💀FosilTRex[D]', '🔶Jeremejevite[E]', '🔹Jade', '🔶FireOpal[A]', '▪️BijihBesi', '▪️BatuKerikil[A]', '🔸Perak[S]', '🔶Benitoite[C]', '🔹Obsidian[S]']
lt2 = ['◻️Kalifornium565[S]', '💀FosilAlien[A]', '◼️BlackDiamond[A]', '🔶Benitoite[S]', '🔶Poudretteite[S]', '🔶FireOpal', '💀FosilTriceratops[A]', '🔹Jamborite[A]', '🔹Rodium[E]', '▪️BatuBara[B]', '🔶Benitoite[B]', '◻️Painite[C]', '🔷RedDiamond[C]', '▪️Batu[S]', '▪️Batu[D]', '🔶RedBeryl[D]', '🔶Benitoite[D]', '◻️Unobtanium[E]', '🔷Alexandrite[E]', '◼️Adamantium', '🔷Serendibite', '◻️Unobtanium', '▪️Topaz[S]', '◻️Magistone', '🔸Perak[E]', '🔹Platina[E]', '🔶Musgravite[A]', '🔹Basalt[B]', '🔶Poudretteite[B]', '◼️Adamantium[C]', '🔶RedBeryl[C]', '🔹Jade[D]', '▪️BatuBara[E]']
lt3 = ['◻️Kalifornium525[S]', '🔷RedDiamond[S]', '🔷Diamond[S]', '🔹Rodium[S]', '🔹Basalt[A]', '🔹Obsidian[A]', '◻️Painite[B]', '🔹Jamborite[B]', '🔹Basalt[C]', '💀FosilTRex[C]', '🔶FireOpal[C]', '◻️Unobtanium[C]', '💀FosilTriceratops[C]', '◼️Vibranium[C]', '🔸Perak[C]', '💀FosilGajahPurba[D]', '💀FosilTriceratops[D]', '◼️BlackDiamond[D]', '◻️Dragonite[D]', '🔸Tembaga[D]', '🔹Jamborite[D]', '🔶Benitoite[E]', '💀FosilVelociraptor[E]', '▪️Topaz[E]', '▪️Batu[E]', '💀FosilGajahPurba[E]']
lt4 = ['💀FosilManusiaPurba[D]', '▪️Topaz[C]', '🔹Opal', '💀FosilGajahPurba[B]', '🔹Jamborite[E]', '💀FosilVelociraptor[S]', '🔷Diamond', '◼️BlackDiamond[E]', '🔷Diamond[C]', '💀FosilManusiaPurba[C]', '◻️Kalifornium545[E]', '🔶RedBeryl[B]', '🔶Musgravite[B]', '▪️BatuKerikil[B]', '🔷Grandidierite[E]', '️▪️BatuKerikil[E]', '◼️Adamantium[E]', '🔹Rodium[C]', '🔹Basalt[D]', '◻️Dragonite[C]', '💀FosilTRex[S]', '▪️BijihBesi[D]', '🔷Taaffeite[E]', '🔷Taaffeite[D]', '◻️Dragonite[S]', '🔹Obsidian', '◻️Valyrium[D]', '💀FosilTRex', '🔷Alexandrite[S]']
lt5 = ['◼️Vibranium[E]', '🔹Obsidian[D]', '▪️BatuBara', '🔹Platina[C]', '🔶Poudretteite[D]', '🔹Platina', '🔶Jeremejevite[D]', '🔹Opal[A]', '🔹Opal[E]', '🔹Iridium[A]', '🔹Opal[D]', '💀FosilVelociraptor[C]', '◻️Unobtanium[D]', '🔷Taaffeite', '💀FosilManusiaPurba[A]', '▪️BatuBara[C]', '🔹Platina[B]', '💀FosilAlien[B]', '🔹Jade[S]', '◻️Unobtanium[A]', '🔹Jade[E]', '💀FosilVelociraptor[B]', '💀FosilTriceratops[B]', '🔶RedBeryl[E]', '🔸Emas', '🔷Diamond[D]', '◻️Kalifornium565', '🔷Taaffeite[C]', '◻️Valyrium[S]']
lt6 = ['🔶Benitoite', '▪️BatuKerikil[D]', '🔹Platina[S]', '🔸Tembaga[A]', '▪️BatuKerikil[S]', '◻️Kalifornium525', '🔷Serendibite[E]', '🔶Benitoite', '◼️Adamantium[B]', '🔶FireOpal[B]', '💀FosilGajahPurba[C]', '🔸Perak[D]', '🔸Emas[E]', '🔶Poudretteite[E]', '🔶Musgravite[E]', '🔸Emas[A]', '▪️Batu', '◻️Painite', '🔹Opal[B]', '💀FosilTriceratops[E]', '🔷RedDiamond[A]', '🔹Jade[B]', '◻️Valyrium', '🔸Emas[D]', '🔸Tembaga[E]', '🔹Rodium[A]', '🔶Jeremejevite[A]', '🔸Tembaga[B]', '💀FosilGajahPurba[S]', '◻️Magistone[S]']
lt7 = ['◻️Kalifornium525[E]', '🔸Perak[A]', '◼️Adamantium[D]', '💀FosilGajahPurba', '▪️BijihBesi[A]', '▪️BatuKerikil', '🔷Alexandrite[C]', '💀FosilNaga[C]', '🔸Emas[B]', '🔷Grandidierite[D]', '🔹Iridium[C]', '🔹Jamborite[C]', '🔹Rodium[D]', '🔹Jade[C]', '💀FosilManusiaPurba[B]', '🔹Rodium', '🔶Poudretteite[C]', '◼️Vibranium[C]', '🔷Serendibite[B]', '▪️BijihBesi[E]', '▪️BijihBesi[B]', '🔹Basalt[E]', '🔸Perak', '💀FosilGajahPurba', '▪️Topaz[D]', '🔹Iridium[D]', '💀FosilVelociraptor[A]', '💀FosilNaga[A]', '💀FosilTRex[A]', '◼️Vibranium[B]', '💀FosilAlien[S]']
lt8 = ['💀FosilVelociraptor', '🔶FireOpal[S]', '🔶Poudretteite', '◼️Vibranium[D]', '◻️Magistone[D]', '▪️BatuBara[S]', '🔶Benitoite[A]', '▪️Batu[B]', '▪️Topaz[A]', '💀FosilManusiaPurba[E]', '💀FosilAlien[E]', '◼️BlackDiamond', '▪️BatuBara[D]', '▪️Topaz', '🔷Alexandrite[D]', '🔹Obsidian[E]', '◻️Painite[E]', '🔸Perak[B]', '🔶RedBeryl[S]', '◻️Unobtanium[S]']
lt9 = ['◻️Painite[D]', '🔷Grandidierite[B]', '🔹Jamborite[S]', '◻️Valyrium[E]', '🔹Basalt[S]', '💀FosilTriceratops[S]', '🔷Grandidierite[A]', '▪️Topaz[B]', '◻️Valyrium[C]', '🔸Tembaga[S]', '🔸Tembaga', '💀FosilNaga[S]', '🔷Taaffeite[S]']
lt10 = ['🔸Tembaga[C]', '💀FosilManusiaPurba', '◼️BlackDiamond[C]', '◻️Dragonite[E]', '◻️Kalifornium545[D]', '🔹Opal[C]', '🔷Grandidierite[S]', '🔷Grandidierite[C]', '▪️Topaz[S]', '◻️Kalifornium565[B]', '🔶Musgravite[S]', '🔹Jamborite', '🔶Jeremejevite[S]', '◻️Kalifornium545[A]']
lt11 = ['🔶Musgravite[D]', '🔷Serendibite[A]', '◼️Vibranium', '🔷Taaffeite[B]', '◻️Kalifornium565[A]', '◻️Kalifornium525[B]', '🔷Diamond[B]', '◻️Unobtanium[B]']
lt12 = ['◻️Kalifornium545', '◻️Kalifornium565[D]', '◻️Painite[A]', '🔶Jeremejevite', '◻️Kalifornium525[A]']
lt13 = ['◻️Kalifornium525[D]', '🔹Rodium[B]', '◻️Magistone[C]', '🔷RedDiamond', '🔸Emas[S]', '◻️Painite[S]']
lt14 = ['◼️Adamantium[A]', '◻️Dragonite[A]', '◼️BlackDiamond[B]']
lt15 = ['◼️Vibranium[A]', '◻️Dragonite[B]']
lt16 = ['🔹Platina[A]', '🔹Opal[S]', '◼️Vibranium[S]']
lt17 = ['🔹Platina[D]', '🔶FireOpal[E]', '💀FosilGajahPurba[A]', '🔷Diamond[A]', '🔷Diamond[E]', '🔶Jeremejevite[B]', '🔷Alexandrite', '💀FosilAlien']
lt18 = ['🔶Musgravite', '🔶RedBeryl', '🔷Grandidierite', '🔹Basalt', '◻️Dragonite', '🔹Iridium[E]', '🔷RedDiamond[E]', '💀FosilNaga[E]', '◻️Kalifornium565[E]', '🔷RedDiamond[D]', '💀FosilVelociraptor[D]', '🔶Jeremejevite[C]', '🔷Serendibite[C]', '▪️BatuKerikil[C]', '🔹Obsidian[C]', '🔷Alexandrite[B]', '🔹Obsidian[B]', '◻️Valyrium[B]', '🔷Alexandrite[A]', '🔷Taaffeite[A]', '▪️Batu[A]', '▪️BatuBara[A]', '🔹Jade[A]', '🔹Iridium[S]', '🔷Serendibite[S]', '💀FosilManusiaPurba[S]', '▪️BijihBesi[S]']

nama = []
misi1 = []
selesai = []
batu = []

with TelegramClient(sesi_fil, api_id, api_hash) as clien:
    clien.loop.run_until_complete(clien.send_message('kampungmaifamxbot', pesan))

    @clien.on(events.NewMessage(from_users='kampungmaifamxbot'))
    async def handler(event):
    
        if 'Gua ini memiliki' in event.raw_text:
            time.sleep(2)
            await event.click(text='⛏⛏⛏')
            return
        
        if 'Kamu mendapat sebuah' in event.raw_text:
            chat = event.raw_text
            m = chat.split()
            p = m[9] in nama
            if p == True:
                misi1.append(1)
                print (misi1)
                if len(misi1) == 3:
                    pesan = '/waisak2567BE_MisiTambang'
                    try:
                        time.sleep(2)
                        await event.respond(pesan)
                    except Exception as q:
                        print ('Error: {}'.format(q))
                else:
                    a = chat.split('.')
                    b, c, d = a
                    e = c.split()
                    e1, e2, e3, e4, e5, e6, e7 = e
                    et = int(e2)
                    time.sleep(et)
                    await event.click(text='⛏⛏⛏')

            if p == False:
                a = chat.split('.')
                b, c, d = a
                e = c.split()
                e1, e2, e3, e4, e5, e6, e7 = e
                et = int(e2)
                time.sleep(et)
                await event.click(text='⛏⛏⛏')
            return
        
        if 'Kamu masih terlalu lelah' in event.raw_text:
            chat = event.raw_text
            f = chat.split('.')
            g, h, i, j = f
            k = i.split()
            k1, k2, k3, k4, k5, k6, k7 = k
            kt = int(k2)
            time.sleep(kt)
            await event.click(text='⛏⛏⛏')
            return
            
        if 'Cek daftar misi' in event.raw_text:
            pesan = event.raw_text
            misi1.clear()
            l = pesan.split()
            #misi = l[5]
            o = l[5] + ','
            nama.append(o)
            print ('Nama dari misi: {}'.format(nama))
            if l[5] in lt1:
                time.sleep(2)
                await event.respond(mine1)
            elif l[5] in lt2:
                time.sleep(2)
                await event.respond(mine2)
            elif l[5] in lt3:
                time.sleep(2)
                await event.respond(mine3)
            elif l[5] in lt4:
                time.sleep(2)
                await event.respond(mine4)
            elif l[5] in lt5:
                time.sleep(2)
                await event.respond(mine5)
            elif l[5] in lt6:
                time.sleep(2)
                await event.respond(mine6)
            elif l[5] in lt7:
                time.sleep(2)
                await event.respond(mine7)
            elif l[5] in lt8:
                time.sleep(2)
                await event.respond(mine8)
            elif l[5] in lt9:
                time.sleep(2)
                await event.respond(mine9)
            elif l[5] in lt10:
                time.sleep(2)
                await event.respond(mine10)
            elif l[5] in lt11:
                time.sleep(2)
                await event.respond(mine11)
            elif l[5] in lt12:
                time.sleep(2)
                await event.respond(mine12)
            elif l[5] in lt13:
                time.sleep(2)
                await event.respond(mine13)
            elif l[5] in lt14:
                time.sleep(2)
                await event.respond(mine14)
            elif l[5] in lt15:
                time.sleep(2)
                await event.respond(mine15)
            elif l[5] in lt16:
                time.sleep(2)
                await event.respond(mine16)
            elif l[5] in lt17:
                time.sleep(2)
                await event.respond(mine17)
            elif l[5] in lt18:
                time.sleep(2)
                await event.respond(mine18)
            return
            
        if 'Berhasil menyelesaikan' in event.raw_text:
            selesai.append(1)
            nama.clear()
            batu.clear()
            print(len(selesai))
            pesan = '/waisak2567BE_MisiTambang'
            try:
                time.sleep(2)
                await event.respond(pesan)
            except Exception as q:
                print ('Error: {}'.format(q))
            return
    
    clien.run_until_disconnected()
    print(time.asctime(), '-', 'Stop')
