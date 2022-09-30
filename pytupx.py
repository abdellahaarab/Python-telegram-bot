# importing the module 
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytube import YouTube , Stream
from telegram.ext import *
from telegram import Update


async def ytb(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # # link of the video to be downloaded 
    # link="https://www.youtube.com/watch?v=PNYfcU5n0-4"
    try: 
        data = YouTube(update.message.text)
        await update.message.reply_photo(data.thumbnail_url)
        await update.message.reply_text(f"""\nTitle: {data.title} \nlength: {data.length} - Views: {data.views}""" )    
        print(f"thes is the id : {str(update.message.id)}")   
    except:
        await update.message.reply_text("An error occurred, Try  again !!")
        
        
