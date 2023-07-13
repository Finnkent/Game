#!/usr/bin/env python3





import time

import asyncio
import os
import sys
os.chdir(sys.path[0])

if f"limit.session" in os.listdir():
    os.remove(f"limit.session")
import threading
from telethon import TelegramClient, events, utils

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_fil = input('Akun: ')

mese = 'SpaceExploration'
restore = '/restore'
abis = 0

with TelegramClient(sesi_fil, api_id, api_hash) as clien:
        clien.loop.run_until_complete(clien.send_message('kampungmaifamxbot', mese))

        @clien.on(events.NewMessage(from_users='kampungmaifamxbot'))
        async def handler(event):

            if 'Kumpulkan mineral sebanyak' in event.raw_text:
                time.sleep(290)
                print(event.raw_text)
                await event.click(text="⛏")
                return

            if 'Proses tambang berlangsung selama' in event.raw_text:
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
                await event.respond(mese)
                return


        clien.run_until_disconnected()
        print(time.asctime(), '-', 'Stop')

threading.Thread(target=fani).start()
print(time.asctime(), '-', 'Start')

#if abis == 2 :
#    client.disconnect()
#    clien.disconnect()
