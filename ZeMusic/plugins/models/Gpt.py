import time
import requests
from pyrogram import Client, filters
from pyrogram.enums import ChatAction, ParseMode
from ZeMusic import app


# استخدام توكن OpenAI API (يجب أن تكون مسجل في OpenAI وتملك مفتاح API)
OPENAI_API_KEY = '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'

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
            prompt = message.text.split(" ", 1)[1]
            
            # إعداد طلب إلى OpenAI API
            headers = {
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json"
            }
            data = {
                "model": "text-davinci-003",
                "prompt": prompt,
                "max_tokens": 150
            }
            
            response = requests.post("https://api.openai.com/v1/completions", headers=headers, json=data)
            
            try:
                response_data = response.json()
                if "choices" in response_data and len(response_data["choices"]) > 0:
                    answer = response_data["choices"][0]["text"]
                    end_time = time.time()
                    telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ms"
                    await message.reply_text(
                        f"{answer.strip()}",
                        parse_mode=ParseMode.MARKDOWN
                    )
                else:
                    await message.reply_text("لم يتم العثور على النتائج في الاستجابة.")
            except KeyError:
                await message.reply_text("حدث خطأ أثناء الوصول إلى الاستجابة.")
    except Exception as e:
        await message.reply_text(f"**Error: {e}**")
