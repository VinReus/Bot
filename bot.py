import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Leggi il TOKEN da Heroku (variabili di configurazione)
TOKEN = os.getenv("TOKEN")

# Comando /pika
def comando_pika(update: Update, context: CallbackContext):
    update.message.reply_text("Pika Pika ??")

# Risposta automatica a "buongiorno"
def messaggio_ricevuto(update: Update, context: CallbackContext):
    testo = update.message.text.lower()
    if "buongiorno" in testo:
        update.message.reply_animation("https://example.com/path/to/your/animation.mp4")  # sostituisci con URL o percorso della tua animazione

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    
    # Comando /pika
    dp.add_handler(CommandHandler("pika", comando_pika))
    
    # Messaggi normali (non comandi)
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, messaggio_ricevuto))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
```
