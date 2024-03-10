import time

from telethon import TelegramClient

channel_link = ""
api_id = 123
api_hash = ""
bot_token = ""

client = TelegramClient("my_bot", api_id=api_id, api_hash=api_hash)
client.start()

with TelegramClient('session_name', api_id, api_hash) as client:
    chat_list = ["https://t.me/testmeBro0"] # здесь находятся рекламные чаты\
    for chat in client.iter_messages("https://t.me/testmeBro0"):
        client.send_message(chat, 'Реклманое сообщение', comment_to=chat)
        print(chat.text)
