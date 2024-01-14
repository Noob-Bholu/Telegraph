# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved Modified By ©️ Team Alexa
""""
Alexa is a Telegram Audio and video streaming bot 
Copyright (c) 2023 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want.
"""

import os
import re
import asyncio
import traceback
from data import AlexaData
from pyrogram.errors import FloodWait
from telegraph import upload_file, Telegraph, exceptions
from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


telegraph = Telegraph()
telegraph.create_account(short_name="The Team Alexa")


## UPLOAD PHOTOS #private

@Client.on_message(filters.photo & filters.private)
async def photo_upload(bot, message):
    msg = await message.reply(AlexaData.UPLOAD_MSG, quote=True)
    download_path = await bot.download_media(
        message=message, file_name="image/jetg"
    )
    try:
        link = upload_file(download_path)
        generated_link = "https://telegra.ph" + "".join(link)
    except:
        await msg.edit_text(
            "🌹 ꜰɪʟᴇ ᴍᴜsᴛ ʙᴇ ʟᴇss ᴛʜᴀɴ 5ᴍʙ, ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɴᴏᴛʜᴇʀ ꜰɪʟᴇ ",
            disable_web_page_preview=True, reply_markup=AlexaData.ERROR_BUTTON)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        IN_BUTTON = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(" 𝐉ᴏɪɴ 𝐔s", url="https://t.me/Intangible_creatorR"),
                InlineKeyboardButton("𝐔ᴘᴅᴀᴛᴇs", url="https://t.me/Intangible_creatorR")
            ],
            [
                InlineKeyboardButton("🌐 ᴡᴇʙ ᴘʀᴇᴠɪᴇᴡ 🌐", url=generated_link)
            ]
        ]
    )
        await t.edit_text(
            f"🖇️ **ʟɪɴᴋ** - `{generated_link} `\n\n<a href=https://youtube.com/Unknown_criteriaA>sᴜʙsᴄʀɪʙᴇ ᴏɴ ʏᴏᴜᴛᴜʙᴇ</a>",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)
#group

@Client.on_message(filters.photo & filters.group)
async def photo_upload(bot, message):
    msg = await message.reply(AlexaData.UPLOAD_MSG, quote=True)
    download_path = await bot.download_media(
        message=message, file_name="image/jetg"
    )
    try:
        link = upload_file(download_path)
        generated_link = "https://telegra.ph" + "".join(link)
    except:
        await msg.edit_text(
            "🌹 ꜰɪʟᴇ ᴍᴜsᴛ ʙᴇ ʟᴇss ᴛʜᴀɴ 5ᴍʙ, ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɴᴏᴛʜᴇʀ ꜰɪʟᴇ ",
            disable_web_page_preview=True, reply_markup=AlexaData.ERROR_BUTTON)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        IN_BUTTON = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(" 𝐉ᴏɪɴ 𝐔s", url="https://t.me/Intangible_creatorR"),
                InlineKeyboardButton("𝐔ᴘᴅᴀᴛᴇs", url="https://t.me/Intangible_creatorR")
            ],
            [
                InlineKeyboardButton("🌐 ᴡᴇʙ ᴘʀᴇᴠɪᴇᴡ 🌐", url=generated_link)
            ]
        ]
    )
        await t.edit_text(
            f"🖇️ **ʟɪɴᴋ** - `{generated_link} `\n\n<a href=https://youtube.com/Unknown_criteriaA>sᴜʙsᴄʀɪʙᴇ ᴏɴ ʏᴏᴜᴛᴜʙᴇ</a>",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)   

## UPLOAD VIDEOS

@Client.on_message(filters.video & filters.private)
async def video_upload(bot, message):
    msg = await message.reply(AlexaData.UPLOAD_MSG, quote=True)
    download_path = await bot.download_media(message=message, file_name="video/jetg")
    try:
        link = upload_file(download_path)
        generated_link = "https://telegra.ph" + "".join(link)
    except:
        await msg.edit_text(
            "🌹 ꜰɪʟᴇ ᴍᴜsᴛ ʙᴇ ʟᴇss ᴛʜᴀɴ 5ᴍʙ, ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɴᴏᴛʜᴇʀ ꜰɪʟᴇ ",
            disable_web_page_preview=True, reply_markup=AlexaData.ERROR_BUTTON)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        IN_BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(" 𝐉ᴏɪɴ 𝐔s", url="https://t.me/itzme_dear"),
                    InlineKeyboardButton("𝐔ᴘᴅᴀᴛᴇs ", url="https://t.me/Intangible_creatorR")
                ],
                [
                    InlineKeyboardButton("🌐 ᴡᴇʙ ᴘʀᴇᴠɪᴇᴡ 🌐", url=generated_link)
                ]
            ]
        )
        await t.edit_text(
            f"🖇️ **ʟɪɴᴋ** - `{generated_link} `\n\n<a href=https://youtube.com/Unknown_criteriaA>sᴜʙsᴄʀɪʙᴇ ᴏɴ ʏᴏᴜᴛᴜʙᴇ</a>",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)


        
## UPLOAD GIF

@Client.on_message(filters.animation & filters.private)
async def animation_upload(bot, message):
    msg = await message.reply(AlexaData.UPLOAD_MSG, quote=True)
    download_path = await bot.download_media(message=message, file_name="gif/jetg")
    try:
        link = upload_file(download_path)
        generated_link = "https://telegra.ph" + "".join(link)
    except:
        await msg.edit_text(
            "🌹 ꜰɪʟᴇ ᴍᴜsᴛ ʙᴇ ʟᴇss ᴛʜᴀɴ 5ᴍʙ, ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɴᴏᴛʜᴇʀ ꜰɪʟᴇ ᴀʟsᴏ ",
            reply_markup=AlexaData.INLINE_SELECT,
            disable_web_page_preview=True)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        IN_BUTTON = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(" 𝐉ᴏɪɴ 𝐔s", url="https://t.me/itzme_dear"),
                InlineKeyboardButton("𝐔ᴘᴅᴀᴛᴇs ", url="https://t.me/Intangible_creatoR")
            ],
            [
                InlineKeyboardButton("🌐 ᴡᴇʙ ᴘʀᴇᴠɪᴇᴡ 🌐", url=generated_link)
            ]
        ]
        )
        await t.edit_text(
            f"🖇️ **ʟɪɴᴋ** - `{generated_link} `\n\n<a href=https://youtube.com/Unknown_criteriaA>sᴜʙsᴄʀɪʙᴇ ᴏɴ ʏᴏᴜᴛᴜʙᴇ</a>",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)