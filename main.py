

from decouple import config

from telegram import Update
from telegram.ext import * #ApplicationBuilder, CommandHandler, ContextTypes
from telegram.ext import filters
import methods as m 
import pytupx as p

print("Startiing...")

BOT_TOKEN = config('token')
app = ApplicationBuilder().token(BOT_TOKEN).build()
#start
app.add_handler(CommandHandler("start", m.start))
#hello
app.add_handler(CommandHandler("hello", m.hello))
#help
app.add_handler(CommandHandler("help", m.help))
#ytb
app.add_handler(MessageHandler(filters.TEXT  , p.ytb))

app.run_polling()

 # link="https://www.youtube.com/watch?v=PNYfcU5n0-4"
   #by abdellah aarab
