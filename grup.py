api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = 'Finnkent'

grup = -1001980862520
teks = '/nextgame@ThirtyOneBot '

with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(grup, teks))
    @client.on(events.NewMessage(chats=-1001980862520))
    async def handler(event):
        message = event.raw_text
        if "Join with the button" in message:
            await event.click(text='Join') 
            return
          
    client.start()
    print(time.asctime(), '-', 'Mulai')
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Berhenti')
