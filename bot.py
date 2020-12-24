# -*- coding: utf-8 -*-
from telethon import TelegramClient, sync, events
import re


api_id = 2591217                  # API ID (получается при регистрации приложения на my.telegram.org)
api_hash = "9a3798e50de53d54d31b1cde0fa2a5b5"              # API Hash (оттуда же)
phone_number = "+380951214072"    # Номер телефона аккаунта, с которого будет выполняться код
client = TelegramClient('session_name', api_id, api_hash)
not_r_count = 0
r_count = 0

@client.on(events.NewMessage(chats=('statistika_baccara')))
async def normal_handler(event):
    global not_r_count, r_count
    msg = event.message.to_dict()['message']
    result = re.search(r"#R", msg)

    if not result:
        if not_r_count < 5:
            not_r_count += 1
        elif not_r_count >= 5:
            not_r_count -= not_r_count
            not_r_count += 1
        print(not_r_count, result)

    else:
        if not_r_count == 4:
            not_r_count += 1
            await client.send_message('Andriuhovici', 'ВЫПАЛА НУЖНАЯ КОМБИНАЦИЯ. 10 #R')

        else:
            not_r_count -= not_r_count
            not_r_count += 1

client.start()
client.run_until_disconnected()
