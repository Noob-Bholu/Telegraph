# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved Modified, Enhanced And Database Added By ©️ Team Alexa
""""
Alexa is a Telegram Audio and video streaming bot 
Copyright (c) 2022 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want.
"""
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

class AlexaData(object):
    STATS = "🌹 **ᴛᴏᴛᴀʟ ᴜsᴇʀs** : {}\n🌹 **ᴛᴏᴛᴀʟ ɢʀᴏᴜᴘs** : {}\n\n**──────────────**\n➛ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ** : `{}`\n**──────────────**"
    BCAST_USG = "**💐 ᴜꜱᴀɢᴇ**:\n`/broadcast` [ᴍᴇꜱꜱᴀɢᴇ] ᴏʀ ʀᴇᴘʟᴀʏ ᴛᴏ ᴍᴇssᴀɢᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ɪɴᴛᴏ ᴄʜᴀᴛs ᴀɴᴅ ᴜsᴇʀs"
    BCAST_DN = "🌹 **ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴍᴇssᴀɢᴇ ɪɴ {} chat(s) and {} user(s).**"
    REPLAY_MSG = "🌹 ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɪɴᴄʟᴜᴅᴇ ᴛᴇxᴛ ᴀꜰᴛᴇʀ ᴛʜᴇ /upload ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ."
    UPLOAD_MSG = "⬆️ ʏᴏᴜʀ ꜰɪʟᴇ ɪs ʙᴇᴇɴ ᴜᴘʟᴏᴀᴅɪɴɢ..."
    UPLOAD_MSG2 = "🌹 ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴍᴇᴅɪᴀ / ᴛᴇxᴛ  / ᴀɴɪᴍᴀᴛɪᴏɴ ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴘʜ . . ."
    HOLD_MSG = "⏳• ʜᴏʟᴅ ᴏɴ ɪ'ᴍ ᴜᴘʟᴏᴀᴅɪɴɢ . . ."
    ERROR_MSG = "🌹 ᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ ꜰɪʟᴇ ꜰᴏʀᴍᴀᴛ ᴏʀ ꜰɪʟᴇ sɪᴢᴇ, ɪᴛ ᴍᴜsᴛ ʙᴇ ʟᴇss ᴛʜᴀɴ 5 ᴍʙ . . ."
    FILE_ERROR = "😢 sᴏʀʀʏ, ᴛʜᴇ ꜰɪʟᴇ ɪs ɴᴏᴛ sᴜᴘᴘᴏʀᴛᴇᴅ !"
    INLINE_SELECT = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🤩 ᴊᴏɪɴ ᴜs", url="https://t.me/Intangible_creatorR"),
                InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs 🐲", url="https://t.me/itzme_dear")
            ]
        ]
    )
    ERROR_BUTTON = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(" 𝐑ᴇᴘᴏʀᴛ 𝐇ᴇʀᴇ", url="https://t.me/Intangible_creatorR"),
                InlineKeyboardButton("𝐉ᴏɪɴ ", url="https://t.me/itzme_dear")
            ]
        ]
    )    
    H_BUTTON = [
         [
              InlineKeyboardButton(text="๏ ᴀʙᴏᴜᴛ ๏", callback_data="ABOUT_CMD"),
         ],
         [
              InlineKeyboardButton(text="๏ ᴄᴍᴅs ๏", callback_data="CMDS_CMD"),
              InlineKeyboardButton(text="๏ ᴛᴇᴀᴍ ᴀʟᴇxᴀ ๏", callback_data="TEAM_CMD"),
         ],
    ]

    HELP_BACK = [
            [     
                  InlineKeyboardButton(text="๏ ʙᴀᴄᴋ ๏", callback_data="HELP_BACK"),
            ],
    ]

    HELP_STRING = f"""
**ʜᴇʀᴇ ʏᴏᴜ ᴄᴀɴ ғɪɴᴅ ʙᴀsɪᴄ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ʜᴇʟᴘ ᴀʟʟ ᴄᴍᴅ ᴀɴᴅ ᴅᴇᴛᴀɪʟs ᴀʀᴇ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ!**
**──────────────**

"""

    ABOUT_STRING = f"""
➛  ᴛʜɪs ɪɴᴄʀᴇᴅɪʙʟᴇ ʙᴏᴛ ᴄᴀɴ ᴇꜰꜰᴏʀᴛʟᴇssʟʏ ᴜᴘʟᴏᴀᴅ ᴘɪᴄᴛᴜʀᴇs, ᴠɪᴅᴇᴏs, ᴀɴɪᴍᴀᴛɪᴏɴs, ᴀɴᴅ ᴛᴇxᴛs ᴏɴ ᴛᴇʟᴇɢʀᴀᴘʜ ᴀɴᴅ ɪɴsᴛᴀɴᴛʟʏ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴡɪᴛʜ ᴀ ᴅɪʀᴇᴄᴛ ʟɪɴᴋ ᴛᴏ ᴛʜᴇ ᴜᴘʟᴏᴀᴅᴇᴅ ꜰɪʟᴇ. ᴊᴜsᴛ ʀᴇᴍᴇᴍʙᴇʀ, ꜰᴏʀ ᴛʜᴇ ʙᴇsᴛ ᴇxᴘᴇʀɪᴇɴᴄᴇ, ᴇɴsᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ꜰɪʟᴇ ɪs ᴜɴᴅᴇʀ 5ᴍʙ ɪɴ sɪᴢᴇ.
**───────────────**

"""

    CMDS_STRING = f"""
<u>**ʜᴇʀᴇ ɪs sᴏᴍᴇ ʙᴀsɪᴄ ᴄᴍᴅs**</u>
**➛ `/stats` ᴄᴏʟʟᴇᴄᴛ ᴄʜᴀᴛs ᴀɴᴅ ᴜsᴇʀ ᴡʜᴇʀᴇ ʙᴏᴛ ɪs ᴡᴏʀᴋɪɴɢ.**
**➛ `/help` ᴛᴏ ᴋɴᴏᴡ ᴀʟʟ ᴀʙᴏᴜᴛ ᴄᴍᴅ ɢɪᴠᴇɴ ɪɴ ᴛʜɪs ʙᴏᴛ.**
**➛ `/start` ᴜsᴇᴅ ᴛᴏ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ.**
**➛ `/upload` ʀᴇᴘʟᴏ ᴛᴏ ᴍᴇssᴀɢᴇ ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴘɪᴄs, ᴠᴅᴏ, ᴀɴɪᴍᴀᴛᴏɴ ᴏɴ ᴛᴇʟᴇɢʀᴀᴘʜ.**
**➛ `/uploadtxt` ʀᴇᴘʟᴀʏ ᴛᴏ ᴍᴇssᴀɢᴇ ᴏʀ ʀᴇᴘʟᴀʏ ᴡɪᴛʜ ᴍᴇssᴀɢᴇ ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴛᴇxᴛ ᴏɴ ᴛᴇʟᴇɢʀᴀᴘʜ.**
**➛ `/broadcast` ʙʀᴏᴀᴅᴄᴀsᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴜsᴇʀs ᴀɴᴅ ᴄʜᴀᴛᴇs.**
**───────────────**

"""

    TEAM_STRING = f"""
ɴᴏᴛʜɪɴɢ ʜᴇʀᴇ
"""    