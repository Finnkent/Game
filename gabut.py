import time 
import asyncio, string
import datetime
import sys, re
import random
import logging
from time import sleep
from datetime import datetime
from telethon import TelegramClient, events, sync, utils
from datetime import datetime, timedelta

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = input("Mau akun mana = ")
client = TelegramClient(sesi_file, api_id, api_hash).start()


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Kirim')

print("\nPilih bot yng digunakan")
mpm = input("\n\tKetik 1 untuk bg1\n\tKetik 2 untuk posko\n   Angka = ")
if mpm == '1':
    chat = client.get_input_entity("BidGroup1")
elif mpm == '2':
    chat = client.get_input_entity("PoskoPengungsianBidGroup")

logging.basicConfig(level=logging.ERROR)

bid = input("Masukkan id lelang : ")
bids = bid.split(',')
print(time.asctime(), '-', "Gas")
for k in bids:
    if '-' in k:
        kirim = k.split('-')
        for i in range(int(kirim[0]), int(kirim[1])+1):
            pesan = '/lelangGroup_'+str(i)+'_1e15'
            client.send_message(chat, pesan)
            print(time.asctime(), '-', str(i))
            countdown(615)
            print("Proses selesai")
    else:
        pesan = '/lelangGroup_'+str(k)+'_1e15'
        client.send_message(chat, pesan)
        print(time.asctime(), '-', str(i))
        countdown(615)
        print("Proses selesai")
        
client.run_until_disconnected()
print(time.asctime(), '-', 'Berhenti')
