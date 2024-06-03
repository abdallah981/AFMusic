import os
import aiohttp
import aiofiles
import yt_dlp
from yt_dlp import YoutubeDL
from pyrogram import Client, filters
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from ZeMusic import app
from ZeMusic.plugins.play.filters import command
import config

stiklok =[]

@app.on_message(command(["قفل البحث","تعطيل البحث"]))
async def block_stickers(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id in stiklok:
            return await message.reply_text(f"البحث مقفل من قبل")
        stiklok.append(message.chat.id)
        return await message.reply_text(f"تم قفل البحث \n\n من قبل ←{message.from_user.mention}")
    else:
        return await message.reply_text(f"الامر يخص المشرف")
    

@app.on_message(filters.command(["فتح البحث","تفعيل البحث"]))
async def block_stickers(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in ["creator", "administrator"]:
        if message.chat.id in stiklok:
            return await message.reply_text(f"البحث مقفل من قبل")
        stiklok.append(message.chat.id)
        return await message.reply_text(f"تم قفل البحث \n\n من قبل ←{message.from_user.mention}")
    else:
        return await message.reply_text(f"الامر يخص المشرف")
    



def remove_if_exists(path):
    if os.path.exists(path):
        os.remove(path)

Nem = config.BOT_NAME + " ابحث"

@app.on_message(command(["/song", "تحميل", "بحث", Nem]))
async def song_downloader(client, message: Message):
    global is_search_enabled
    if not is_search_enabled:
        await message.reply_text("<b>البحث معطل حاليًا.</b>")
        return
    query = " ".join(message.command[1:])
    m = await message.reply_text("<b>⇜ جـارِ البحث عـن المقطـع الصـوتـي . . .</b>")
    ydl_ops = {
        'format': 'bestaudio[ext=m4a]',
        'keepvideo': True,
        'prefer_ffmpeg': False,
        'geo_bypass': True,
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': True,
    }
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"

        # تحميل الصورة المصغرة وحفظها بشكل غير متزامن
        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    async with aiofiles.open(thumb_name, mode='wb') as f:
                        await f.write(await resp.read())
        
        duration = results[0]["duration"]

    except Exception as e:
        await m.edit("- لم يتم العثـور على نتائج ؟!\n- حـاول مجـدداً . . .")
        print(str(e))
        return

    await m.edit("<b>⇜ جـارِ التحميل ▬▭ . . .</b>")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        
        rep = f"𖡃 ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ʙʏ \n@{app.username} "
        host = str(info_dict["uploader"])
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        
        await m.edit("<b>⇜ جـارِ التحميل ▬▬ . . .</b>")
        
        # التأكد من وجود الملف الصوتي قبل الإرسال
        if os.path.exists(audio_file):
            try:
                await message.reply_audio(
                    audio=audio_file,
                    caption=rep,
                    title=title,
                    performer=host,
                    thumb=thumb_name,
                    duration=dur,
                )
                await m.delete()
            except Exception as e:
                await m.edit("حدث خطأ أثناء إرسال الملف الصوتي. يرجى المحاولة مرة أخرى لاحقًا.")
                print(f"Error while sending audio file: {e}")
        else:
            await m.edit("حدث خطأ أثناء تحميل الملف الصوتي. لم يتم العثور على الملف.")
            print("Audio file not found after download.")

    except Exception as e:
        await m.edit("حدث خطأ أثناء تحميل الملف الصوتي. يرجى المحاولة مرة أخرى لاحقًا.")
        print(f"Error while downloading audio: {e}")

    try:
        remove_if_exists(audio_file)
        remove_if_exists(thumb_name)
    except Exception as e:
        print(f"Error while cleaning up files: {e}")

# أمر لتعطيل البحث
@app.on_message(command(["تعطيل البحث"]))
async def disable_search(client, message: Message):
    global is_search_enabled
    is_search_enabled = False
    await message.reply_text("<b>تم تعطيل البحث بنجاح.</b>")

# أمر لتفعيل البحث
@app.on_message(command(["تفعيل البحث"]))
async def enable_search(client, message: Message):
    global is_search_enabled
    is_search_enabled = True
    await message.reply_text("<b>تم تفعيل البحث بنجاح.</b>")
