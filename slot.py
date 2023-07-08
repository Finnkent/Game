import time, asyncio, sys, random

from telethon import TelegramClient, events, utils, Button

api_id = 18850178 
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = input('Akun : ')

cmd = '/th_SlotMachine_SevenFish'
cmd1 = '/th_SlotMachine_add'
bot = 'KampungMaifamBot'
me = 'Maifam'
invest = '/invest_JetPribadi_beli_100'
ch = 'inMaifam'

jackpot = 0
gems = 0
tiket = 0 
poin = 0
jala = 0
ikan = 0
skill = 0
cv = 0
sk = 0
fp = 0 
mm = 0 
hw = 0 
af = 0 

print("Pilih slot mode:")
mpm = input("\t1. Sevenfish \n\t2. SixLeaves\n\nPilih = ")


if mpm == '1':
    cmd = '/th_SlotMachine_SevenFish'
elif mpm == '2':
    cmd = '/th_SlotMachine_SixLeaves'

with TelegramClient(sesi_file, api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message(bot, cmd))
        @client.on(events.NewMessage(from_users=bot))
        async def handler(event):
            global jackpot
            global gems
            global tiket
            global poin 
            global jala
            global ikan
            global skill
            global cv
            global sk
            global af
            global fp
            global hw
            global mm
            
            me = await client.get_me()
            
            dn = me.first_name
            usn = me.username
            
            if '1900000Qn' in event.raw_text:
                time.sleep(2)
                await event.respond('/tamanHiburan_TembakTopeng')
                print('Mulai Dart')
                return
            
            if 'kemampuan+1' in event.raw_text:
                sk += 1
            
            if '1 PoinJackpot' in event.raw_text:
                jackpot += 1
                
            if '1000💎' in event.raw_text:
                gems += 1000
                
            if '10000💎' in event.raw_text:
                gems += 10000
                
            if '1 PoinSlot' in event.raw_text:
                poin += 1
                
            if '3 PoinSlot' in event.raw_text:
                poin += 3
                
            if '5 PoinSlot' in event.raw_text:
                poin += 5
                
            if '10 PoinSlot' in event.raw_text:
                poin += 10
                
            if '20 PoinSlot' in event.raw_text:
                poin += 20
                
            if '25 PoinSlot' in event.raw_text:
                poin += 25
                
            if '30 PoinSlot' in event.raw_text:
                poin += 30
                
            if '50 PoinSlot' in event.raw_text:
                poin += 50
                
            if '60 PoinSlot' in event.raw_text:
                poin += 25
                
            if '100 PoinSlot' in event.raw_text:
                poin += 100
                
            if '100 UmpanJala' in event.raw_text:
                jala += 100
                
            if '1000 UmpanJala' in event.raw_text:
                jala += 1000
            
            if '2500 PoinIkan' in event.raw_text:
                ikan += 2500
                
            if '25000 PoinIkan' in event.raw_text:
                ikan += 25000
            
            if '10000 KemampuanMemancing' in event.raw_text:
                skill += 10000
                
            if '100000 KemampuanMemancing' in event.raw_text:
                skill += 100000
                
            if '1000000 KemampuanMemancing' in event.raw_text:
                skill += 1000000
            
            if '100 🎫Tiket' in event.raw_text:
                tiket += 100
                
            if '10 🎫Tiket' in event.raw_text:
                tiket += 10
                
            if '1🏵' in event.raw_text:
                cv += 1
                
            if '2🏵' in event.raw_text:
                cv += 2
                
            if '3🏵' in event.raw_text:
                cv += 3
                
            if 'Berhasil mengumpulkan 30 CollectibleFragment SixLeaves!! Kamu memperoleh: 🧌ActionFigure' in event.raw_text:
                af += 1
                
            if 'Berhasil mengumpulkan 30 CollectibleFragment SixLeaves!! Kamu memperoleh: 🏎HotWheels' in event.raw_text:
                hw += 1
                
            if 'Berhasil mengumpulkan 30 CollectibleFragment SixLeaves!! Kamu memperoleh: 👾FunkoPop' in event.raw_text:
                fp += 1
                
            if 'Berhasil mengumpulkan 30 CollectibleFragment SixLeaves!! Kamu memperoleh: 🤖MechaModel' in event.raw_text:
                mm += 1
                
            elif 'Ada tujuh jenis ikan' in event.raw_text:
                time.sleep(2)
                await event.click(1,0)
                return
            
            elif 'Ada enam jenis daun' in event.raw_text:
                time.sleep(2)
                await event.click(1,0)
                return
            
            elif 'Kamu memutar SlotMachine 10x' in event.raw_text:
                time.sleep(2)
                await event.click(1,0)
                return
            
            elif 'Koin untuk' in event.raw_text:
                if mpm == '1':
                    time.sleep(2)
                    await event.respond(cmd1)
                    return
                else:
                    time.sleep(2)
                    await event.respond("/collectibleFragment_SixLeaves")
                    return
            
            elif 'Kumpulkan 30 CollectibleFragment' in event.raw_text:
                time.sleep(2)
                await event.click(text="Get CollectibleItem")
                time.sleep(2)
                await event.respond(cmd1)
                return
            
            elif 'Apa kamu' in event.raw_text:
                time.sleep(2)
                await event.click(text="Confirm")
                return
            
            elif 'Berhasil membeli tambahan' in event.raw_text:
                time.sleep(2)
                await event.respond(cmd)
                return
            
            elif 'Setiap harinya' in event.raw_text:
                time.sleep(2)
                await event.click(text='Mulai')
                return
 
            elif 'Pilih sasaran' in event.raw_text:
                time.sleep(2)
                await event.click(0,1)
                return
            
            elif 'Lemparanmu berhasil' in event.raw_text:
                time.sleep(2)
                await event.click(text='Lanjut')
                return
            
            elif 'Sayang sekali' in event.raw_text:
                time.sleep(2)
                await event.click(text='Lanjut')
                return
            
            elif 'Kesempatan' in event.raw_text:
                
                finalresult = """
🎡 <b>TamanHiburan:</b> {} - @{} 

🎰 <b>Poin Jackpot:</b> <i>+{}</i>
💎 <b>Gem:</b> <i>+{}</i>
🎫 <b>Tiket:</b> <i>+{}</i>
🏅 <b>Poin Slot:</b> <i>+{}</i>
🛥 <b>Umpan Jala:</b> <i>+{}</i>
🎣 <b>Poin Ikan:</b> <i>+{}</i>
⚓️ <b>Kemampuan Memancing:</b> <i>+{}</i>
🏵 <b>Carnival Poin:</b> <i>+{}</i>
🎯 <b>Kemampuan Dart:</b> <i>+{}</i>
🧌 <b>Action Figure:</b> <i>+{}</i>
🤖 <b>Mecha Model:</b> <i>+{}</i>
👾 <b>Funko Pop:</b> <i>+{}</i>
🏎 <b>Hot Wheels:</b> <i>+{}</i>

<b>Mode:</b> <code>{}</code> 
<b>Waktu selesai:</b> <code>{}</code>
"""
                
                time.sleep(2)
                await event.respond(invest)
                time.sleep(2)
                await client.send_message(ch, ''
                + str(finalresult).format(
                    dn,
                    usn,
                    jackpot,
                    gems,
                    tiket,
                    poin,
                    jala,
                    ikan,
                    skill,
                    cv,
                    sk,
                    af,
                    mm,
                    fp,
                    hw,
                    cmd,
                    time.asctime()) + '',
                parse_mode= 'html'
                )
                return
            
            elif 'investasi termahal' in event.raw_text:
                time.sleep(2)
                print('--Selesai--')
                exit


        client.start()
        print(time.asctime(), '-', 'Slot Started')
        client.run_until_disconnected()
	
