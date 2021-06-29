# Infinity Bots

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait

@Client.on_message(filters.document & filters.channel)
async def caption(client, message: Message):
    await message.edit("🤗 Uploaded by @Anime_Wars.\n😄 Group: @Anime_Chat_English. ",
          reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Channel", url="https://t.me/Anime_Wars)]
            ]
                                           )
                      )
