# Telegram get members public group and send messages to it
Python scripting with Telegram API usage

## Installation (Windows 10)
1. Download get_members.py, send_message.py, config.py files and move it to any location
2. Open CMD console (Hotkey WIN+R, and type 'cmd')
3. Type command in console: 'pip install telethon'

## Obtain Telegram API ID and HASH
1. Read instruction: https://core.telegram.org/api/obtaining_api_id#obtaining-api-id
2. Set up api_id, api_hash, phone in config.py

## Using
1. Set up public group name in get_members.py
2. Start script get_members.py in Explorer or by CMD command: python get_members.py
3. Now in this folder created file group_members.csv
4. Prepare this csv and split for 20-25 contacts per one bulk send messages
5. Set up message text in send_message.py and set up name of csv file
6. Start script send_message.py in Explorer or by CMD command: python send_message.py

That's all.
