import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Leggi il TOKEN da Heroku (config vars)
TOKEN = os.getenv("TOKEN")

# ? Comando /Pika
def comando_pika(update: Update, context: CallbackContext):
    update.message.reply_text("Pika Pika ??")

# ? Risposta automatica a "buongiorno"
def messaggio_ricevuto(update: Update, context: CallbackContext):
    testo = update.message.text.lower()

    if "buongiorno" in testo:
        update.message.reply_animation("https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    # Comando /pika
    dp.add_handler(CommandHandler("pika", comando_pika))

    # Messaggi normali (no comandi)
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, messaggio_ricevuto))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()