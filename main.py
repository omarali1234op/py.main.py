"""




       ███████╗ ██╗ ████████╗ ██╗  ██╗  ██████╗  ███╗   ██╗
       ██╔════╝ ██║ ╚══██╔══╝ ██║  ██║ ██╔═══██╗ ████╗  ██║
       █████╗   ██║    ██║    ███████║ ██║   ██║ ██╔██╗ ██║
       ██╔══╝   ██║    ██║    ██╔══██║ ██║   ██║ ██║╚██╗██║
       ███████╗ ██║    ██║    ██║  ██║ ╚██████╔╝ ██║ ╚████║
       ╚══════╝ ╚═╝    ╚═╝    ╚═╝  ╚═╝  ╚═════╝  ╚═╝  ╚═══╝

codded by : mohmmad || Telegram : @l_b10 - @EITHON1

"""

from pyrogram import Client, filters
from pyrogram.types import Message
from telegraph import upload_file
import os
app=Client(
    "MediaToTelegraphLink",
    api_id = "12421436",
    api_hash = "fbe8061f1148eabbacdf9e0713e8b74a",
    bot_token = '5617535290:AAF-jVB0riU_Bgn_CqIjBZy9SwM5m95uWD0'
)

@app.on_message(filters.command('start') & filters.private)
async def start(client, message):
    text = f"""
**› مرحبًا  {message.from_user.mention},
› انا بوت تحويل الميديا لرايط مباشر
مقدم من سورس فيجا 
SOURCE VEGA : @SOURCEVEGA
Dav : @l_b10
› الصيغ المدعومة : 'jpeg', 'jpg', 'png', 'mp4' ، 'gif'.**

**› [- source vega by : ali ♡](tg://user?id=5385468134)**
            """
    await app.send_message(message.chat.id, text, disable_web_page_preview=True)
    

@app.on_message(filters.media & filters.private)
async def glink(client, message):
    try:
        text = await message.reply("› جار المعالجة...")
        async def progress(current, total):
            await text.edit_text(f"📥 جار التحميل... {current * 100 / total:.1f}%")
        try:
            location = f"./media/private/"
            lo = await message.download(location, progress=progress)
            await text.edit_text("📤 جار الرفع ...")
            up = upload_file(lo) 
            await text.edit_text(f"**🌐 | رابط تليجراف **:\n\n<code>https://telegra.ph{up[0]}</code>")     
            os.remove(lo) 
        except Exception as e:
            await text.edit_text(f"**❌ | حدث خطأ **\n\n<i>**السبب**: {e}</i>")
            os.remove(lo) 
            return                 
    except Exception:
        pass        
                      

print("Programmed by : @l_b10🇸🇾")
app.run()
