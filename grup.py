from telethon.sync import TelegramClient, events

api_id = '18850178'
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'

session_name = 'Finnkent'

group_id = -1001943370596
join_command = '.joinvcg'

client = TelegramClient(session_name, api_id, api_hash)


def start_voice_chat(group):
    client.send_message(group, join_command)


@client.on(events.NewMessage(chats=group_id))
async def handle_message(event):
    if event.raw_text == join_command and event.sender_id == client.get_me().id:
        await client.start_voice_chat(group_id)


with client:
    client.run_until_disconnected()