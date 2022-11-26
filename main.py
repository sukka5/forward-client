from pyrogram import Client, filters
from pyrogram.types import Message


RUN = {"isRunning": True}
User = Client(
    'pyrogram',
    api_hash="a0539f94d7e13d3ba3296f56a4da1f2e",
    api_id=10499076,
    bot_token="5949478819:AAGsm_rLjJPbfDfJYpaDlhMeSeYpb-2nlKU"
)

@User.on_message(filters.incoming & filters.command(['start']))
async def startHandler(bot, message):
    await message.reply_text(f"{message.from_user.mention} Welcome1")

User.run()



















