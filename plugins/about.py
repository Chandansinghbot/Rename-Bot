import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"ʙᴏᴛ ɴᴀᴍᴇ: :- <a href='https://t.me/Premium_RenameBot'>ʀᴇɴɢᴏᴋᴜ</a>\nᴄʀᴇᴀᴛᴏʀ:- <a href='https://t.me/god_luffy_ati'>🦋 ɪᴛ'ꜱ ʟᴜғғʏ 🦋</a>\nʟᴀɴɢᴜᴀɢᴇ: ᴘʏᴛʜᴏɴ3\nꜱᴇʀᴠᴇʀ: ᴋᴏʏᴇʙ\nᴛᴏᴛᴀʟ ʀᴇɴᴀᴍᴇᴅ ꜰɪʟᴇ:- {total_rename}\nᴛᴏᴛᴀʟ ꜱɪᴢᴇ ʀᴇɴᴀᴍᴇᴅ:- {humanbytes(int(total_size))} \n\nᴛʜᴀɴᴋ ʏᴏᴜ [ɪᴛ'ꜱ ʟᴜғғʏ](https://t.me/god_luffy_ati) ꜰᴏʀ ʏᴏᴜʀ ʜᴀʀᴅ ᴡᴏʀᴋ\n\nᴡᴇ ʟᴏᴠᴇ ʏᴏᴜ [ʀᴇɴɢᴏᴋᴜ](https://t.me/elitecraft_support) ❤️",quote=True)
