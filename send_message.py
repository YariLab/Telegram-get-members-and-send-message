from telethon.sync import TelegramClient
import csv
import config

api_id = config.api_id
api_hash = config.api_hash
phone = config.phone

client = TelegramClient(phone, api_id, api_hash)

async def get_last_message(user):
    messages = await client.get_messages(user, limit=1)
    return messages[0].message if messages else ''

# Limit to 25 messages per day to non-mutual contacts!
# if account pre-banned - max 3 messages per 12 hours!
# if account banned - thats all ;(
async def send_messages(file_name, message):
    await client.start()
    
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:

                user = row['username'] if row['username'] else int(row['id'])
                last_message = await get_last_message(user)
                if last_message != '':
                    print(f"Last message with {row['first_name']} {row['last_name']}: {last_message}")
                else:
                    await client.send_message(user, message, silent=True) # silent message
                    print(f"Message sent to {row['first_name']} {row['last_name']}")
            except Exception as e:
                print(f"Failed to send message to {row['first_name']} {row['last_name']}: {e}")

# **Bold**
# __Italic__
# ~~Strike~~
# `Monospace`
# ```Code```
#
# \n - new row 
#
# Example:
text = "**Bold**, __italic__, ~~strike~~ text\n"
monospace = "it's `monospace`\n"
inline_code = "it's inline code: ```let i = 0;```\n"
code = """a = 1
b = 6
res = a + b
print(f\"result: {res}\")
"""
multiline_code = f"it's multiline code: ```{code}```\n"
link = "it's link: [link](https://google.com)"

message = f"{text}{monospace}{inline_code}{multiline_code}{link}"
file_name = 'group_members.csv'

with client:
    client.loop.run_until_complete(send_messages(file_name, message))
