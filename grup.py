import asyncio
from telethon import TelegramClient, events

# Inisialisasi bot Telegram Client
api_id = '18850178'
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
client = TelegramClient('Finnkent', api_id, api_hash)

# Command yang digunakan untuk bergabung ke voice chat
join_command = '/joinvcg'


async def start_voice_chat(group_id):
    await client.send_message(group_id, join_command)

# Event handler untuk pesan baru dalam grup
@client.on(events.NewMessage())
async def handle_message(event):
    if event.raw_text == join_command and event.is_group and event.sender_id == event.sender_id:
        await client.join_call(event.chat_id)

# Event handler untuk perintah '/mulai'
@client.on(events.NewMessage(pattern='/mulai'))
async def handle_start_command(event):
    await event.respond('Mulai...')
    await start_voice_chat(event.chat_id)

# Event handler untuk perintah '/keluarvcg'
@client.on(events.NewMessage(pattern='/keluarvcg'))
async def handle_exit_command(event):
    # Menggunakan metode leave_call untuk keluar dari voice chat group 
    await client.leave_call(event.chat_id)
    await event.respond('Keluar dari Voice Chat Group.')

# Menjalankan bot Telegram
with client:
    client.run_until_disconnected()