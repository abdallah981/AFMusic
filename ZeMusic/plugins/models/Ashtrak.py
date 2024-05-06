from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button
from pyrogram.enums import ChatType
from pyrogram.errors import UserNotParticipant
from ZeMusic import app

channel = "e5_52"

async def subscription(_, __: Client, message: Message):
    user_id = message.from_user.id
    try: 
        await app.get_chat_member(channel, user_id)
    except UserNotParticipant: 
        return False
    return True
    
subscribed = filters.create(subscription)

app.on_message(filters.command(["تشغيل", "شغل"]) & ~subscribed)
async def checker(_: Client, message: Message):
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        user_id = message.from_user.id
        user = message.from_user.first_name
        markup = Markup([
            [Button("𝐒𝐎𝐔𝐑𝐂𝐄 𝐊𝐈𝐍𝐆", url=f"https://t.me/{channel}")]
        ])
        await message.reply(
            f"عذرًا عزيزي {user}، عليك الاشتراك في قناة البوت أولاً.",
            reply_markup=markup
        )
