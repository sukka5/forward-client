from pyrogram import Client, filters
from pyrogram.types import Message

user = Client(
    'pyrogram',
    api_hash="a0539f94d7e13d3ba3296f56a4da1f2e",
    api_id=10499076,
    bot_token="5949478819:AAGsm_rLjJPbfDfJYpaDlhMeSeYpb-2nlKU"
)

@user.on_message(filters.incoming & filters.private & filters.command(['start']))
async def startHandler(bot:Client, msg:Message):
    await msg.reply_text(
        text = f'**Welcome {msg.from_user.mention}!**',
        quote = True
    )


print("working")
user.run()
