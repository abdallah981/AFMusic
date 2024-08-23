import platform
import re
import socket
import uuid
import os
import speedtest
import asyncio
import platform
from sys import version as pyver
from datetime import datetime

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.errors import MessageIdInvalid, FloodWait
from pyrogram.types import CallbackQuery, InputMediaPhoto, Message, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from pytgcalls.__version__ import __version__ as pytgver
from ZeMusic import app
import config
from config import OWNER_ID
from ZeMusic import YouTube, app
from ZeMusic import app as Client
from ZeMusic.core.userbot import assistants
from ZeMusic.misc import SUDOERS, mongodb
from ZeMusic.plugins import ALL_MODULES
from ZeMusic.utils.database import get_served_chats, get_served_users, get_sudoers
from ZeMusic.utils.decorators.language import language, languageCB
from ZeMusic.utils.inline.stats import back_stats_buttons, stats_buttons
from config import BANNED_USERS


loop = asyncio.get_running_loop()


@app.on_message(filters.command(["《hshdhh》"], "") & SUDOERS)
@language
async def stats_global(client, message: Message, _):
    upl = stats_buttons(_, True if message.from_user.id in SUDOERS else False)
    await message.reply_photo(
        photo=config.STATS_IMG_URL,
        caption=_["gstats_2"].format(config.MUSIC_BOT_NAME),
        reply_markup=upl,
    )
    


@app.on_message(filters.command(["《hsjsnsnsnj》", "كيب المطور", "/keb"], "") & SUDOERS & filters.private)
async def kep(client, message):
  kep = ReplyKeyboardMarkup([["《قسم الاذاعه》"], ["《قسم الحساب المساعد》"], ["《قسم الادمنيه》", "《قسم الكولات》"], ["《معلومات السيرفر》", "《فحص سرعه البوت》"], ["المحظورين عام🚨", "المحظورين ميوزك❌"], ["《الاحصائيات والتواصل》"], ["《قسم الاشتراك الاجباري》"], ["نقل ملكية البوت"], ["《قسم النسخه الاحتياطيه》"], ["《قسم السورس》"], ["《الغاء》", "《تنظيف》"], ["《قفل الكيبورد🔒》"]], resize_keyboard=True)
  await message.reply_text("╮⦿ اهـلا بڪ عزيـزي المطـور الاساسـي │⎋ اليك كيب التحكم بالبوت في سورس الميوزك❤️‍🔥", reply_markup=kep)
    


@Client.on_message(filters.command(["《قسم الحساب المساعد》"], "") & SUDOERS & filters.private)
async def helpercn(client, message):
   userbot = await get_client(1)
   me = await userbot.get_me()
   i = f"@{me.username} : {me.id}" if me.username else me.id
   b = await client.get_chat(me.id)
   b = b.bio if b.bio else "لا يوجد بايو"
   kep = ReplyKeyboardMarkup([["فحص المساعد 🎗️"], ["تغير الاسم الاول 🪧", "تغير الاسم التاني 📝"], ["تغير البايو 🔖"], ["تغير اسم المستخدم 🔰"], ["اضافه صوره 🖼️", "• ازاله صوره •"], ["رجوع"], ["《الغاء》"]], resize_keyboard=True)
   await message.reply_text(f"**أهلا بك عزيزي المطور **\n**هنا قسم الحساب المساعد **\n**{me.mention}**\n**{i}**\n**{b}**", reply_markup=kep)



@Client.on_message(filters.command(["《قسم الاذاعه》"], "") & SUDOERS & filters.private)
async def cast(client: Client, message):
    kep = ReplyKeyboardMarkup([["《اذاعة》", "《اذاعة بالتثبيت》"], ["《اذاعة بالتوجيه》"], ["《اذاعة بالمجموعات》", "《اذاعة بالتثبيت بالمجموعات》"], ["رجوع"], ["《الغاء》"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الاذاعه تحكم بالازار**", reply_markup=kep)



@Client.on_message(filters.command(["《قسم الادمنيه》"], "") & SUDOERS & filters.private)
async def cast(client: Client, message):
    kep = ReplyKeyboardMarkup([["رفع ادمن", "تنزيل ادمن"], ["قائمه الأدمنيه"], ["رجوع"], ["《الغاء》"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الادمنيه تحكم بالازار**", reply_markup=kep)



@Client.on_message(filters.command(["《قسم الاشتراك الاجباري》"], "") & SUDOERS & filters.private)
async def cast(client: Client, message):
    kep = ReplyKeyboardMarkup([["《تفعيل الاشتراك》", "《تعطيل الاشتراك》"], ["《ضع قناة الاشتراك》", "《حذف قناة الاشتراك》"], ["《قناة الاشتراك》"], ["رجوع"], ["《الغاء》"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا • قسم الاشتراك الاجباري • تحكم بالازار**", reply_markup=kep)



@Client.on_message(filters.command(["《قسم النسخه الاحتياطيه》"], "") & SUDOERS & filters.private)
async def cast(client: Client, message):
    kep = ReplyKeyboardMarkup([["الأدمنية", "الجروبات"], ["المستخدمين"], ["رجوع"], ["《الغاء》"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا • قسم النسخه الاحتياطيه •  تحكم بالازار**", reply_markup=kep)



@Client.on_message(filters.command(["《قسم السورس》"], "") & SUDOERS & filters.private)
async def cast(client: Client, message):
    kep = ReplyKeyboardMarkup([["《مطور السورس》", "《السورس》"], ["《جروب السورس》"], ["رجوع"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا • قسم النسخه الاحتياطيه •  تحكم بالازار**", reply_markup=kep)



@Client.on_message(filters.command(["《الاحصائيات والتواصل》"], "") & SUDOERS & filters.private)
async def cast(client: Client, message):
    kep = ReplyKeyboardMarkup([["《الاحصائيات》"], ["《تفعيل التواصل》", "《تعطيل التواصل》"], ["رجوع"], ["《الغاء》"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم • الاحصائيات • تحكم بالازار**", reply_markup=kep)



@Client.on_message(filters.command(["《قسم الكولات》"], "") & SUDOERS & filters.private)
async def cast(client: Client, message):
    kep = ReplyKeyboardMarkup([["الكولات النشطه 🗣️⁩"], ["الفيديوهات النشطه 📢"], ["رجوع"], ["《الغاء》"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الكولات تحكم بالازار**", reply_markup=kep)



@Client.on_message(filters.command(["اذاعه عام ♻️⁩"], "") & SUDOERS)
async def loooo(client: Client, message):
     name = await client.ask(message.chat.id, "• ارسل الان الاذاعه •")
     text = name.text
     await name.reply_text("جاري بدا الاذاعه انتظر بعض الوقت")
     chats = await get_served_chats()
     users = await get_served_users()
     chat = []
     dn = 0
     fd = 0
     for user in users:
         chat.append(int(user["user_id"]))
     for c in chats:
         chat.append(int(c["chat_id"]))
     for i in chat:
         try:
           m = await client.send_message(chat_id=i, text=text)
           dn += 1
         except FloodWait as e:
                    flood_time = int(e.x)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
         except Exception as e:
                    fd += 1
                    continue
     return await message.reply_text(f"**تمت الاذاعه بنجاح .✅**\n\n**تمت الاذاعه الي : {dn}**\n**وفشل : {fd}**")


@Client.on_message(filters.command(["توجيه عام 📊"], "") & SUDOERS)
async def looooooo(client: Client, message):
     name = await client.ask(message.chat.id, "• ارسل الان التوجيه •")
     text = name.text
     await name.reply_text("جاري بدا الاذاعه انتظر بعض الوقت")
     chats = await get_served_chats()
     users = await get_served_users()
     chat = []
     dn = 0
     fd = 0
     for user in users:
         chat.append(int(user["user_id"]))
     for c in chats:
         chat.append(int(c["chat_id"]))
     for i in chat:
         try:
           m = await client.forward_messages(i, message.chat.id, name.message_id)
           dn += 1
         except FloodWait as e:
                    flood_time = int(e.x)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
         except Exception as e:
                    fd += 1
                    continue
     return await message.reply_text(f"**تمت التوجيه بنجاح .✅**\n\n**تمت التوجيه الي : {dn}**\n**وفشل : {fd}**")



@Client.on_message(filters.command("فحص المساعد 🎗️", "") & SUDOERS)
async def userrrrr(client: Client, message):
    mm = await message.reply_text("Collecting stats")
    start = datetime.now()
    u = 0
    g = 0
    sg = 0
    c = 0
    b = 0
    a_chat = 0
    client = await get_client(1)
    Meh=await client.get_me()
    usere = Meh.username
    group = ["supergroup", "group"]
    async for dialog in client.get_dialogs():
        if dialog.chat.type == "private":
            u += 1
        elif dialog.chat.type == "bot":
            b += 1
        elif dialog.chat.type == "group":
            g += 1
        elif dialog.chat.type == "supergroup":
            sg += 1
            user_s = await dialog.chat.get_member(int(Meh.id))
            if user_s.status in ("creator", "administrator"):
                a_chat += 1
        elif dialog.chat.type == "channel":
            c += 1

    end = datetime.now()
    ms = (end - start).seconds
    await mm.edit_text(
        """**ꜱᴛᴀᴛꜱ ꜰᴇᴀᴛᴄʜᴇᴅ ɪɴ {} ꜱᴇᴄᴏɴᴅꜱ ✅**
✅**ʏᴏᴜ ʜᴀᴠᴇ {} ᴘʀɪᴠᴀᴛᴇ ᴍᴇꜱꜱᴀɢᴇꜱ.**
🏷️**ʏᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ {} ɢʀᴏᴜᴘꜱ.**
🏷️**ʏᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ {} ꜱᴜᴘᴇʀ ɢʀᴏᴜᴘꜱ.**
🏷️**ʏᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ {} ᴄʜᴀɴɴᴇʟꜱ.**
🏷️**ʏᴏᴜ ᴀʀᴇ ᴀᴅᴍɪɴꜱ ɪɴ {} ᴄʜᴀᴛꜱ.**
🏷️**ʙᴏᴛꜱ ɪɴ ʏᴏᴜʀ ᴘʀɪᴠᴀᴛᴇ = {}**
⚠️**ꜰᴇᴀᴛᴄʜᴇᴅ ʙʏ ᴜꜱɪɴɢ @{} **""".format(
            ms, u, g, sg, c, a_chat, b, usere
        )
    )



@Client.on_message(filters.command(["تغير الاسم الاول 🪧", "الاسم الاول"], "") & SUDOERS)
async def changefisrt(client: Client, message):
   try:
    if message.text == "تغير الاسم الاول 🪧":
      return await message.reply_text("• الان قم بالرد علي الاسم الجديد باستخدام كلمه الاسم الاول •")
    name = message.reply_to_message.text
    client = await get_client(1)
    await client.update_profile(first_name=name)
    await message.reply_text("**تم تغير اسم الحساب المساعد بنجاح .✅**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير الاسم")



@Client.on_message(filters.command(["تغير الاسم التاني 📝", "الاسم التاني"], "") & SUDOERS)
async def changelast(client: Client, message):
   try:
    if message.text == "تغير الاسم التاني 📝":
      return await message.reply_text("• الان قم بالرد علي الاسم الجديد باستخدام كلمه الاسم التاني •")
    name = message.reply_to_message.text
    client = await get_client(1)
    await client.update_profile(last_name=name)
    await message.reply_text("**تم تغير اسم الحساب المساعد بنجاح .✅**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير الاسم ")



@Client.on_message(filters.command(["تغير البايو 🔖", "البايو الجديد"], "") & SUDOERS)
async def changebio(client: Client, message):
   try:
    if message.text == "تغير البايو 🔖":
      return await message.reply_text("• الان قم بالرد علي البايو الجديد باستخدام كلمة البايو الجديد •")
    name = message.reply_to_message.text
    client = await get_client(1)
    await client.update_profile(bio=name)
    await message.reply_text("**تم تغير البايو بنجاح .✅**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير البايو ")



@Client.on_message(filters.command(["تغير اسم المستخدم 🔰", "اليوزر"], "") & SUDOERS)
async def changeusername(client: Client, message):
   try:
    if message.text == "تغير اسم المستخدم 🔰":
      return await message.reply_text("• الان قم بالرد علي اليوزر الجديد بدون علامة @ باستخدام كلمه اليوزر •")
    name = message.reply_to_message.text
    client = await get_client(1)
    await client.set_username(name)
    await message.reply_text("**تم تغير اسم المستخدم بنجاح .✅**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير اسم المستخدم")



@Client.on_message(filters.command(["اضافه صوره 🖼️", "الصوره الجديده"], "") & SUDOERS)
async def changephoto(client: Client, message):
   try:
    if message.text == "اضافه صوره 🖼️":
      return await message.reply_text("• الان قم بالرد علي الصورة الجديدة بكلمه الصوره الجديده •")
    m = message.reply_to_message
    photo = await m.download()
    client = await get_client(1)
    await client.set_profile_photo(photo=photo)
    await message.reply_text("**تم تغير صوره الحساب المساعد بنجاح .✅**") 
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير الصوره")



@Client.on_message(filters.command(["• ازاله صوره •"], "") & SUDOERS)
async def changephotos(client: Client, message):
       try:
        client = await get_client(1)
        photos = await client.get_profile_photos("me")
        await client.delete_profile_photos([p.file_id for p in photos[1:]])
        await message.reply_text("**تم ازاله صوره بنجاح .✅**")
       except Exception as es:
         await message.reply_text(f" حدث خطأ أثناء ازاله الصوره")



@Client.on_message(filters.command(["《تنظيف》"], "") & SUDOERS)
async def clean(client: Client, message):
    try:
        await message.delete()
    except:
        pass
    downloads = os.path.realpath("downloads")
    down_dir = os.listdir(downloads)
    pth = os.path.realpath(".")
    os_dir = os.listdir(pth)

    if down_dir:
        for file in down_dir:
            os.remove(os.path.join(downloads, file))
    if os_dir:
        for lel in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg *.png")
    await message.reply_text("» ᴀʟʟ ᴛᴇᴍᴘ ᴅɪʀᴇᴄᴛᴏʀɪᴇs ᴄʟᴇᴀɴᴇᴅ.")


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("**⇆ ʀᴜɴɴɪɴɢ ᴅᴏᴡɴʟᴏᴀᴅ sᴩᴇᴇᴅᴛᴇsᴛ...**")
        test.download()
        m = m.edit("**⇆ ʀᴜɴɴɪɴɢ ᴜᴩʟᴏᴀᴅ sᴩᴇᴇᴅᴛᴇsᴛ...**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**↻ sʜᴀʀɪɴɢ sᴩᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs...**")
    except Exception as e:
        return m.edit(e)
    return result



@Client.on_message(filters.command(["《فحص سرعه البوت》"], "") & SUDOERS)
async def spedtest(client: Client, message):
    m = await message.reply_text("**» ʀᴜɴɴɪɴɢ sᴩᴇᴇᴅᴛᴇsᴛ...**")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""✯ **sᴩᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs** ✯
    
<u>**❥͜͡ᴄʟɪᴇɴᴛ :**</u>
**» __ɪsᴩ :__** {result['client']['isp']}
**» __ᴄᴏᴜɴᴛʀʏ :__** {result['client']['country']}
  
<u>**❥͜͡sᴇʀᴠᴇʀ :**</u>
**» __ɴᴀᴍᴇ :__** {result['server']['name']}
**» __ᴄᴏᴜɴᴛʀʏ :__** {result['server']['country']}, {result['server']['cc']}
**» __sᴩᴏɴsᴏʀ :__** {result['server']['sponsor']}
**» __ʟᴀᴛᴇɴᴄʏ :__** {result['server']['latency']}  
**» __ᴩɪɴɢ :__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=result["share"], caption=output
    )
    await m.delete()



@Client.on_message(filters.command(["《معلومات السيرفر》"], "") & SUDOERS)
async def serverinfoo(client: Client, message):
    sysrep = await message.reply_text(
        f"ɢᴇᴛᴛɪɴɢ {MUSIC_BOT_NAME} sʏsᴛᴇᴍ sᴛᴀᴛs, ɪᴛ'ʟʟ ᴛᴀᴋᴇ ᴀ ᴡʜɪʟᴇ..."
    )
    try:
        await message.delete()
    except:
        pass
    sudoers = len(SUDOERS)
    mod = len(ALL_MODULES)
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(socket.gethostname())
    architecture = platform.machine()
    processor = platform.processor()
    mac_address = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    sp = platform.system()
    ram = str(round(psutil.virtual_memory().total / (1024.0**3))) + " ɢʙ"
    p_core = psutil.cpu_count(logical=False)
    t_core = psutil.cpu_count(logical=True)
    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)}ɢʜᴢ"
        else:
            cpu_freq = f"{round(cpu_freq, 2)}ᴍʜᴢ"
    except:
        cpu_freq = "ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ"
    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.0**3)
    total = str(total)
    used = hdd.used / (1024.0**3)
    used = str(used)
    free = hdd.free / (1024.0**3)
    free = str(free)
    platform_release = platform.release()
    platform_version = platform.version()

    await sysrep.edit_text(
        f"""
➻ <u>**{MUSIC_BOT_NAME} sʏsᴛᴇᴍ sᴛᴀᴛs**</u>

**ᴩʏᴛʜᴏɴ :** {pyver.split()[0]}
**ᴩʏʀᴏɢʀᴀᴍ :** {pyrover}
**ᴩʏ-ᴛɢᴄᴀʟʟs :** {pytgver}
**sᴜᴅᴏᴇʀs :** `{sudoers}`
**ᴍᴏᴅᴜʟᴇs :** `{mod}`

**ɪᴘ :** {ip_address}
**ᴍᴀᴄ :** {mac_address}
**ʜᴏsᴛɴᴀᴍᴇ :** {hostname}
**ᴘʟᴀᴛғᴏʀᴍ :** {sp}
**ᴘʀᴏᴄᴇssᴏʀ :** {processor}
**ᴀʀᴄʜɪᴛᴇᴄᴛᴜʀᴇ :** {architecture}
**ᴘʟᴀᴛғᴏʀᴍ ʀᴇʟᴇᴀsᴇ :** {platform_release}
**ᴘʟᴀᴛғᴏʀᴍ ᴠᴇʀsɪᴏɴ :** {platform_version}

        <b><u>sᴛᴏʀᴀɢᴇ</b><u/>
**ᴀᴠᴀɪʟᴀʙʟᴇ :** {total[:4]} ɢɪʙ
**ᴜsᴇᴅ :** {used[:4]} ɢɪʙ
**ғʀᴇᴇ :** {free[:4]} ɢɪʙ

**ʀᴀᴍ :** {ram}
**ᴩʜʏsɪᴄᴀʟ ᴄᴏʀᴇs :** {p_core}
**ᴛᴏᴛᴀʟ ᴄᴏʀᴇs :** {t_core}
**ᴄᴩᴜ ғʀᴇǫᴜᴇɴᴄʏ :** {cpu_freq}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="ᴄʟᴏsᴇ",
                        callback_data=f"forceclose abc|{message.from_user.id}",
                    ),
                ]
            ]
        ),
    )


@Client.on_message(filters.command(["《قفل الكيبورد🔒》"], "") & SUDOERS)
async def keplook(client: Client, message):
          m = await message.reply("**- تم اخفاء الازرار بنجاح\n- لو تبي تطلعها مرة ثانية اكتب  /keb**", reply_markup= ReplyKeyboardRemove(selective=True))
          
 
