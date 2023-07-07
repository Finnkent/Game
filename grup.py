import asyncio
from telethon import TelegramClient, events

# Inisialisasi Client
api_id = '18850178'
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
client = TelegramClient('Finnkent', api_id, api_hash)

group_id = -1001943370596
join_command = '/joinvcg'

async def start_voice_chat():
    await client.send_message(group_id, join_command)

@client.on(events.NewMessage(chats=group_id))
async def handle_message(event):
    if event.raw_text == join_command and event.sender_id == (await client.get_me()).id:
        await client.start_call(group_id)

@client.on(events.NewMessage(pattern='/mulai', chats=group_id))
async def handle_start_command(event):
    await event.reply('Mulai...')
    await start_voice_chat()

@client.on(events.NewMessage(pattern='/keluarvcg', chats=group_id))
async def handle_exit_command(event):
    # Menggunakan metode leave_call untuk keluar dari voice chat group 
    await client.leave_call(group_id)
    await event.reply('Keluar dari Voice Chat Group.')

async def main():
    # Menunggu sampai client siap
    await client.start()
    await client.run_until_disconnected()

name = None

if name == 'main':
    asyncio.run(main())

with client:
    client.run_until_disconnected()