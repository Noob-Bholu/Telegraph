from pyrogram import Client, filters,enums,idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ChatAction, ParseMode
import openai
from pyrogram.types import CallbackQuery
from config import *
import os,sys,re,requests
import asyncio,time
from random import choice
from bardapi import Bard
from datetime import datetime
import logging

FORMAT = "[NOOB-BHOLU] %(message)s"
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


StartTime = time.time()
Mukesh = Client(
    "Telegraph" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)
xa = bytearray.fromhex("68 74 74 70 73 3A 2F 2F 67 69 74 68 75 62 2E 63 6F 6D 2F 4E 6F 6F 62 2D 6D 75 6B 65 73 68 2F 43 68 61 74 67 70 74 2D 62 6F 74").decode()
SOURCE = xa
MAIN = [
    [
        InlineKeyboardButton(text=" 𝐃ᴇᴠᴇʟᴏᴘᴇʀ ", url=f"https://t.me/{OWNER_USERNAME}"),
        InlineKeyboardButton(text=" 𝐒ᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(
            text="𝐀ᴅᴅ 𝐌ᴇ 𝐈ɴ 𝐔ʀ 𝐆ʀᴘ",
            url=f"https://t.me/ChatGpt_A_Robot?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text=" 𝐇ᴇʟᴘ & 𝐂ᴍᴅs ", callback_data="HELP"),
        InlineKeyboardButton(text=" 𝐔ᴘᴅᴀᴛᴇs ", url=f"https://t.me/{UPDATE_CHNL}"),
    ],
]
#main
openai.api_key = OPENAI_KEY
@Mukesh.on_message(filters.command(["chatgpt","ai","ask"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def chat(bot, message):

    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`/ask 𝐖ʜᴀᴛ 𝐈s 𝐌ᴀᴛʜᴇᴍᴀᴛɪᴄs?`")
        else:
            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL,messages=[{"role": "user", "content": a}],
    temperature=0.2)
            x=resp['choices'][0]["message"]["content"]
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_text(f"➥ {message.from_user.first_name} 𝐀ꜱᴋᴇᴅ:\n\n {a} \n\n➥ {BOT_NAME} 𝐀ɴꜱᴡᴇʀᴇᴅ:-\n\n {x}\n\n➥ 𝐓ɪᴍᴇ 𝐓ᴀᴋᴇɴ  {telegram_ping} \n\n➥ 𝐏ᴏᴡᴇʀᴇᴅ 𝐁ʏ @Intangible_creatorR 🖤", parse_mode=ParseMode.MARKDOWN,reply_markup=InlineKeyboardMarkup(X))     
    except Exception as e:
        await message.reply_text(f"**𝐄ʀʀᴏʀ: {e} \n\n➥ 𝐑ᴇᴘᴏʀᴛ 𝐇ᴇʀᴇ:- @Intangible_creatorR")

  openai.api_key = OPENAI_KEY
@Mukesh.on_message(filters.command(["image","photo","img","gen"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"] ))
async def chat(bot, message):
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        if len(message.command) < 2:
            await message.reply_text(
            "**Example:**\n\n`/gen 𝐓ᴏ 𝐆ᴇɴᴀʀᴀᴛᴇ 𝐘ᴏᴜʀ 𝐃ᴇsɪʀᴇᴅ 𝐏ɪᴄᴛᴜʀᴇ`")
        else:
            a = message.text.split(' ', 1)[1]
            response= openai.Image.create(prompt=a ,n=1,size="1024x1024")
            image_url = response['data'][0]['url']
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_photo(image_url,caption=f"➥ 𝐓ɪᴍᴇ 𝐓ᴀᴋᴇɴ {telegram_ping} \n\n➥ 𝐏ᴏᴡᴇʀᴇᴅ 𝐁ʏ:- @Intangible_creatorR ",parse_mode=ParseMode.DISABLED,reply_markup=InlineKeyboardMarkup(X)) 
    except Exception as e:
            await message.reply_text(f"**ᴇʀʀᴏʀ: **  ` {e} ` \n\n➥ 𝐑ᴇᴘᴏʀᴛ 𝐇ᴇʀᴇ:- @Noob_Nholu ")
openai.api_key = OPENAI_KEY
@Mukesh.on_message(filters.command(["text","audiototext","lyrics"],  prefixes=["","+", ".", "/", "-", "?", "$","#","&"]))
async def chat(bot, message):

    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if message.reply_to_message and message.reply_to_message.media:

            m = await message.reply_to_message.download(file_name="rahul.mp3")
            audio_file = open(m, "rb")
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
            x=transcript["text"]
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_text(f"`{x}` \n➥ 𝐓ɪᴍᴇ 𝐓ᴀᴋᴇɴ {telegram_ping} \n\n➥ 𝐏ᴏᴡᴇʀᴇᴅ 𝐁ʏ:- @UNKNOWN_CRITERIA_RK")     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: **  ` {e} `")



s = bytearray.fromhex("68 74 74 70 73 3A 2F 2F 67 69 74 68 75 62 2E 63 6F 6D 2F 4E 6F 6F 62 2D 6D 75 6B 65 73 68 2F 43 68 61 74 67 70 74 2D 62 6F 74").decode()
