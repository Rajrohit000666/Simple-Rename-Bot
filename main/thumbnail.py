from pyrogram import Client, filters 
from config import ADMIN, temp

@Client.on_message(filters.private & filters.command("set") & filters.user(ADMIN))                            
async def set_tumb(bot, msg):
    replied = msg.reply_to_message
    if not replied:
        await msg.reply("use this command with Reply to a photo")
        return
    if not msg.reply_to_message.photo:
       await msg.reply("Oops !! this is Not a photo")
       return
    Tumb = msg.reply_to_message.photo.file_id
    temp.THUMBNAIL = Tumb
    return await msg.reply(f"Temporary Thumbnail saved✅️ \nDo You want permanent thumbnail. \n\n`{Tumb}` \n\n👆👆 please add this id to your server enviro with key=`THUMBNAIL`")            


@Client.on_message(filters.private & filters.command("view") & filters.user(ADMIN))                            
async def del_tumb(bot, msg):
    if temp.THUMBNAIL:AgACAgUAAxkDAAMRY02geBxvffyz4hM9_IbopbRqac0AAsOxMRvoGiBWMPSDzt0l_2QACAEAAwIAA3kABx4E
        await msg.reply_photo(photo=temp.THUMBNAIL, caption="this is your current thumbnail")
    else:
        await msg.reply_text(text="you don't have any thumbnail")
