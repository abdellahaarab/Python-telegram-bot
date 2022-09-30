# importing the module 
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytube import YouTube , Stream
from telegram.ext import *
from telegram import Update


async def ytb(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    # # link of the video to be downloaded 
    # link="https://www.youtube.com/watch?v=xWOoBJUqlbI"
  
    try: 
        data = YouTube(update.message.text)
        
        # Vidios1 = InlineKeyboardButton(text="Vidios", callback_data="v10")
        # Audio1 = InlineKeyboardButton(text="Audio", callback_data="a10")
        # kebord = InlineKeyboardMarkup().add(Vidios1 , Audio1)
        
        # await update.message.reply_photo(data.thumbnail_url)
        await update.message.reply_text(f"""\nTitle: {data.title} \nlength: {data.length} - Views: {data.views}""" )
        # await update.message.reply_poll("Choose One ",["Vidios","Audio"], is_anonymous=True)
        await update.message.reply_video(data.streaming_data['formats'][1]["url"])


        
        # await update.edited_message()
        # await update.message.reply_text(data.length)
        # await update.message.reply_text(data.streaming_data['formats'][1]["url"])
        # await update.message.reply_audio(data.streaming_data["adaptiveFormats"]["initRange"]["url"])
        
        print(f"thes is the id : {str(update.message.id)}")   
    except:
        await update.message.reply_text("An error occurred, Try  again !!") 
    #     print("Connection Error") #to handle exception 
  
    # # filters out all the files with "mp4" extension 
    # mp4files = yt.filter('mp4') 
  
    # #to set the name of the file
    # yt.set_filename('GeeksforGeeks Video')
      
  
    # # get the video with the extension and
    # # resolution passed in the get() function 
    # d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
    # try: 
    #     # downloading the video 
    #     # d_video.download(SAVE_PATH)
    #     await update.message.reply_text(f"Try contacting @amfih3bot ") 
    # except: 
    #     await update.message.reply_text(f"Try contacting @amfih3bot ")  
 