# Infinity Bots

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait

@Client.on_message(filters.document & filters.channel)
async def caption(client, message: Message):
    await message.edit("Manga Channel: @MangaSee.",
          reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Group", url="https://t.me/Anime_Chat_English")]
            ]
                                           )
                      )
