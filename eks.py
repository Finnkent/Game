from time import sleep, asctime
from telethon.sync import TelegramClient

def send_messages(accounts, lahan, usn, msg, msg2, api_id, api_hash):
    while(True):
        print(f'{asctime()} - Planting starting...')
        for acc in accounts:
            with TelegramClient(acc, api_id, api_hash) as client:
                print(f'Memuat user {acc}:')
                try:
                    print('Sending Message...')
                    client.send_message(usn, msg2)
                    sleep(10)
                    for group in lahan:
                        client.send_message(group, msg)
                        sleep(10)
                except Exception as e:
                    print(f'error : {e} ')
        print(f'{asctime()} - Cooldown...')
        sleep(86400)

accounts = list(map(str,range(1,16)))
lahan = ['BidGroup1']
usn = 'mochamuk'
msg = '/buatLelang_MiniBacon_10'
msg2 = 'Masuk'
#msg2 = '/buatLelang_MiniBacon_10'
api_id = 'your_api_id'
api_hash = 'your_api_hash'

send_messages(accounts, lahan, usn, msg, msg2, api_id, api_hash)