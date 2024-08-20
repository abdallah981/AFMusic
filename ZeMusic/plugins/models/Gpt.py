import random
import time
import requests
from ZeMusic import app
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters

@app.on_message(filters.command(["لوي"], ""))
async def chat_gpt(bot, message):
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "⟡ استخدم الأمر هكذا :\n\n ⟡ لوي + سؤالك"
            )
        else:
            a = message.text.split(" ", 1)[1]  # هنا نضع محدد للمساحة
            response = requests.get(f"https://chatgpt.apinepdev.workers.dev/?question={a}")

            try:
                if "answer" in response.json():
                    x = response.json()["answer"]
                    end_time = time.time()
                    telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ms"
                    await message.reply_text(
                        f"{x}",
                        parse_mode=ParseMode.MARKDOWN
                    )
                else:
                    await message.reply_text("لم يتم العثور على النتائج في الاستجابة.")
            except KeyError:
                await message.reply_text("حدث خطأ أثناء الوصول إلى الاستجابة.")
    except Exception as e:
        await message.reply_text(f"**Error: {e}**")
