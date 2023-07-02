from telethon import TelegramClient, events, sync, utils
import asyncio, string, time
from time import sleep

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
accounts = [
    '01',
    '02',
    '03',
    '04',
    '05',
    '06',
    '07',
    '08',
    '09',
    '10',
    '11',
    '12',
    '13',
    '14',
    '15',
]

lahan = [
    'BidGroup1',

]

usn = 'mochamuk'
msg = '/endbid'
msg2 = 'Masuk'
#msg2 = '/buatLelang_MiniBacon_10'

while(True):
    print(time.asctime(), '-', '\nPlanting starting...')
    for x in accounts:
        client = TelegramClient(x, api_id, api_hash).start()
        try:
            print('Memuat user {}:'.format(x))
            # client.connect()
            print('Sending Message...')
            for x in range(1):
                client.send_message(usn,msg2)
                time.sleep(10)
            for y in lahan:
                client.send_message(y,msg)
                time.sleep(10)
            client.disconnect()
            time.sleep(10)
            
        except Exception as e:
            print('error : {} '.format(e))
    print(time.asctime(), '-', 'Cooldown...')
    time.sleep(86400)