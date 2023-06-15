import time
import asyncio
import sys
from telethon import TelegramClient, events, utils

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = input('User: ')
print('Loading...')
print('-' * 40)

mepam = 'kampungmaifamxbot'
krj = '/sg_KeranjangBuah'
gabung = '/sg_gabung'
panen = '/sg_panen'
akt = '/act_CropsMerger'
akt2 = '/act_SkyFarmer'
sghc = '/sg_hc'
masak = '/masak_minibacon_220'

c = [] #jumlah merger
c2 = [] #jumlah panen
g = [] #target act crops merger
g2 = [] #target act sky farmer
h = [] #tanaman sg yang jumlahnya lebih dari 15
i = [] #nomor tanaman yang dimerger
q = [] #daftar koleksi panen sky garden yang diperkirakan sudah bisa klaim hadiah

with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(mepam, masak))
    @client.on(events.NewMessage(from_users=mepam))
    async def handler(event):
        if 'Berhasil memasak' in event.raw_text:
            time.sleep(2)
            await event.respond(masak)
            return
        if 'Kamu tidak bisa memasak' in event.raw_text:
            time.sleep(2)
            await event.respond(akt)
            return
        if 'Panen berbagai buah dari kebun subur' in event.raw_text:
            print(time.asctime())
            print('-' * 40)
            i.clear()
            time.sleep(2)
            await event.respond(panen)
            return
        if 'Tidak ada yang bisa dipanen' in event.raw_text:
            time.sleep(2)
            await event.respond(krj)
            return
        if 'KeranjangBuah 🧺 SkyGarden' and 'Gabungkan buah-buahan' in event.raw_text:
            time.sleep(2)
            await event.respond(gabung)
            return
        if 'menggabungkan buah dari keranjang buah' in event.raw_text:
            pesan = event.raw_text
            a = pesan.split('x') #memecah pesan dari bot dengan pembatas x
            a.pop(-1) #menghapus item terakhir dari list
            for x in a:
                y = x.split() #memecah x dengan pembatas spasi
                z = int(y[-1]) #y[-1] dijadikan integer
                if z >= 15:
                    w = int(z/15)
                    for v in range(w):
                        h.append(y[-2]) #jika integer dari y[-1] lebih dari 15, maka y[-2] ditambahkan ke list h
            time.sleep(2)
            if len(h) >= 1:
                await event.respond(h[0]) #jika jumlah item di list h lebih dari 1, maka respondnya adalah h[0]
            else:
                time.sleep(2)
                await event.respond(sghc)
            return
        if '🥕 /sg_merge_Wortel' in event.raw_text:
            pesan = event.raw_text
            b = pesan.split('x') #memecah pesan dari bot dengan pembatas x
            b.pop(0) #menghapus item pertama dari list
            b.pop(-1) #menghapus item terakhir dari list
            for x in b:
                y = x.split()
                z = int(y[-1])
                if z >= 15:
                    w = int(z/15)
                    for v in range(w):
                        h.append(y[-2])
            print('Total yang akan digabung: {}\n'.format(len(h)))
            return
        if 'Keranjang buah tidak mencukupi,' in event.raw_text:
            time.sleep(5)
            await event.respond(krj)
            return
        if 'Hasil panen dikirim ke' in event.raw_text:
            pesan = event.raw_text
            panen1 = pesan.split('x')
            panen1.pop(-1)
            for x in panen1:
                y = x.split()
                z = int(y[-1])
                c2.append(z)
            time.sleep(5)
            if sum(c2) >= g2[-1]:
                await event.respond(akt2)
            else:
                await event.respond(krj)
            return
        if '15 untuk mendapat 5' in event.raw_text:
            time.sleep(1.5)
            await event.click(text='Gabung 15')
            return
        if 'Berhasil menggabungkan' in event.raw_text:
            c.append(15)
            pesan = event.raw_text
            d = pesan.split()
            #d[-1] = jumlah tanaman
            #d[1] = nama tanaman
            i.append(1)
            print('{:<4} - {}'.format(len(i), d[2])) 
            if len(h) >= 1:
                h.pop(0)
            time.sleep(2)
            if sum(c) >= g[-1]:
                await event.respond(akt)
            else:
                try:
                    await event.respond(h[0])
                except:
                    print(' ')
                    print('+ CropsMerger mulai dari awal run: {}'.format(sum(c)))
                    print('+ SkyFarmer mulai dari awal run: {}'.format(sum(c2)))
                    print('-' * 40)
                    await event.respond(masak)
            return
        if 'tidak memiliki' in event.raw_text:
            if len(h) >= 1:
                h.pop(0)
            time.sleep(2)
            try:
                await event.respond(h[0])
            except:
                await event.respond(sghc)
            return
        if 'Kumpulkan bonus uang dan gelar spesial' in event.raw_text:
            pesan = event.raw_text
            if '✅' in pesan:
                t = pesan.split()
                u = t.index('✅')
                q.append(t[u-2])
                time.sleep(2)
                r = q[0] + '_claim'
                await event.respond(r)
            else:
                time.sleep(2)
                await event.respond('SG')
            return
        if 'Berhasil mengklaim bonus misi' in event.raw_text:
            time.sleep(2)
            s = q[0] + '_unlock'
            await event.respond(s)
            return
        if 'Sekarang kamu bisa memulai misi' in event.raw_text:
            time.sleep(2)
            if len(q) >= 1:
                q.pop(0)
            await event.respond(sghc)
            return
        if 'CropsMerger - CatatanAktivitas' in event.raw_text:
            pesan = event.raw_text
            p = pesan.split()
            n = p[-2].split('(')
            m = n[1].split(')')
            l = m[0].split('/')
            #l[0] = proses act
            #l[1] = target act
            ll0 = int(l[0])
            ll1 = int(l[1])
            if ll1 <= ll0:
                time.sleep(2)
                await event.click(text='Claim')
            else:
                o = ll1 - ll0
                g.append(o)
                time.sleep(2)
                try:
                    await event.respond(h[0])
                except:
                    await event.respond(akt2)
            return
        if 'Berhasil menyelesaikan CropsMerger' in event.raw_text:
            time.sleep(2)
            g.clear()
            c.clear()
            await event.respond(akt)
            return
        if 'SkyFarmer - CatatanAktivitas' in event.raw_text:
            pesan = event.raw_text
            p = pesan.split()
            n = p[-2].split('(')
            m = n[1].split(')')
            l = m[0].split('/')
            #l[0] = proses act
            #l[1] = target act
            ll0 = int(l[0])
            ll1 = int(l[1])
            if ll1 <= ll0:
                time.sleep(2)
                await event.click(text='Claim')
            else:
                o = ll1 - ll0
                g2.append(o)
                time.sleep(2)
                try:
                    await event.respond(h[0])
                except:
                    await event.respond(sghc)
            return
        if 'Berhasil menyelesaikan SkyFarmer' in event.raw_text:
            time.sleep(2)
            g2.clear()
            c2.clear()
            await event.respond(akt2)
            return
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stop')
