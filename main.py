#pylint:disable=C0114
import logging
import os
from pyrogram import Client
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest
# import asyncio
# from pyrogram.errors import FloodWait
# from pyrogram.handlers import MessageHandler
# os.environ['TZ'] = 'Asia/Kolkata'



logging.basicConfig(level=logging.INFO)



bot = Client(
    'bot',
    api_id=27783398, #get it from https://my.telegram.org/auth
    api_hash="4168283cc4de703c9ec1b4f9e0ee4d64", #get it from https://my.telegram.org/auth
    bot_token="6829667414:AAEEzffT0z4rG1ZbxYCNNOgpsrIRd1pf0m8", #get it from @Botfather
    plugins=dict(root="plugins"),
    parse_mode="html")


try:
    bot.run()
except Exception as e:
    print(e)
        
