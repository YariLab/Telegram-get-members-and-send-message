from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
import csv
import config

api_id = config.api_id
api_hash = config.api_hash
phone = config.phone

client = TelegramClient(phone, api_id, api_hash)

async def main():
    await client.start()
    
    # set up public group name below
    group = 'public_group_name'
    
    participants = []
    
    offset = 0
    limit = 100

    while True:
        participants_chunk = await client(GetParticipantsRequest(
            group, ChannelParticipantsSearch(''), offset, limit,
            hash=0
        ))
        if not participants_chunk.users:
            break
        participants.extend(participants_chunk.users)
        offset += len(participants_chunk.users)
    
    with open('group_members.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'username', 'first_name', 'last_name'])
        for user in participants:
            print(f"user: {user}\n")
            writer.writerow([user.id, user.username, user.first_name, user.last_name])

with client:
    client.loop.run_until_complete(main())
