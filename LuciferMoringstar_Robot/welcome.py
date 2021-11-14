import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, User



@Client.on_message(filters.new_chat_members)
async def welcome(bot,message):
	chatid= message.chat.id
    LuciferMoringstar=await bot.send_message(text=f"Welcome {message.from_user.mention} to {message.chat.username} ,  Happy to have here",chat_id=chatid)
        await asyncio.sleep(60) # in seconds
        await LuciferMoringstar.delete()
    else:
        await msg.delete()
@Client.on_message(filters.left_chat_member)
async def goodbye(bot,message):
        chatid= message.chat.id
    LuciferMoringstar=await bot.send_message(text=f"Bye ,  {message.from_user.mention} , Have a Nice Day",chat_id=chatid)
        await asyncio.sleep(60) # in seconds
        await LuciferMoringstar.delete()
    else:
        await msg.delete()
	

