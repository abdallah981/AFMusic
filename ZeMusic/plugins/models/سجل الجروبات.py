from pyrogram import Client, filters
from pyrogram.types import Message, ChatType
from ZeMusic import app
from ZeMusic.utils.database import get_served_chats
from config import LOGGER_ID


async def lul_message(chat_id: int, message: str):
    await app.send_message(chat_id=chat_id, text=message)


@app.on_message(filters.new_chat_members | filters.command("start"))
async def on_new_chat_members(client: Client, message: Message):
    me = await client.get_me()
    chat_id = message.chat.id
    chat_title = message.chat.title
    served_chats = len(await get_served_chats())

    # تحقق من نوع الدردشة داخل الدالة
    if message.chat.type in [ChatType.SUPERGROUP, ChatType.GROUP]:
        if me.id in [user.id for user in message.new_chat_members]:
            added_by = message.from_user.first_name if message.from_user else "مستخدم غير معروف"
            added_id = message.from_user.id

            cont = (await client.get_chat(chat_id)).members_count
            chatusername = f"@{message.chat.username}" if message.chat.username else "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
            lemda_text = f"🌹 تمت اضافه البوت الى مجموعة جديدة.\n\n┏━━━━━━━━━━━━━━━━━┓\n┣★ <b>𝙲𝙷𝙰𝚃</b> › : {chat_title}\n┣★ <b>𝙲𝙷𝙰𝚃 𝙸𝙳</b> › : {chat_id}\n┣★ <b>𝙲𝙷𝙰𝚃 𝚄𝙽𝙰𝙼𝙴</b> › : {chatusername}\n┣★ <b>𝙲𝙾𝚄𝙽𝚃</b> › : {cont}\n┣★ <b>𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃</b> › : {served_chats}\n┣★ <b>𝙰𝙳𝙳𝙴𝙳 𝙱𝚈</b> › :\n┗━━━ꪜ <a href='tg://user?id={added_id}'>{added_by}</a>"
            await lul_message(LOGGER_ID, lemda_text)

    elif message.chat.type == ChatType.CHANNEL:
        # محاولة الحصول على عدد المشتركين في القناة
        try:
            cont = (await client.get_chat(chat_id)).members_count
        except:
            cont = "غير معروف"
        
        # محاولة الحصول على اسم المستخدم الذي أضاف البوت
        added_by = message.from_user.first_name if message.from_user else "غير معروف"
        
        channel_username = f"@{message.chat.username}" if message.chat.username else "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ"
        lemda_text = f"🌹 تمت اضافه البوت الى قناة جديدة.\n\n┏━━━━━━━━━━━━━━━━━┓\n┣★ <b>𝙲𝙷𝙰𝙽𝙽𝙴𝙻</b> › : {chat_title}\n┣★ <b>𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙸𝙳</b> › : {chat_id}\n┣★ <b>𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚄𝙽𝙰𝙼𝙴</b> › : {channel_username}\n┣★ <b>𝙲𝙾𝚄𝙽𝚃</b> › : {cont}\n┣★ <b>𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃</b> › : {served_chats}\n┣★ <b>𝙰𝙳𝙳𝙴𝙳 𝙱𝚈</b> › : {added_by}\n┗━━━━━━━━━━━━━━━━━┛"
        await lul_message(LOGGER_ID, lemda_text)
