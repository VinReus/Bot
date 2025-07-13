import os
import asyncio
from aiohttp import web
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.environ["BOT_TOKEN"]
APP_URL = os.environ["APP_URL"]

GIF_URL = "https://media.giphy.com/media/ASd0Ukj0y3qMM/giphy.gif"

async def handle_buongiorno(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text.lower() == "buongiorno":
        await update.message.reply_animation(GIF_URL)

import os

async def handle_bro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("DEBUG: handle_bro triggered")
    if update.message:
        print(f"DEBUG: Received text: {update.message.text}")
        if update.message.text.lower() == "bro":
            print("DEBUG: Trying to send photo...")
            print("DEBUG: Current dir:", os.getcwd())
            print("DEBUG: Files here:", os.listdir())
            if "bro.jpg" not in os.listdir():
                await update.message.reply_text("Errore: bro.jpg non trovato!")
                return
            try:
                with open("bro.jpg", "rb") as photo:
                    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo)
                print("DEBUG: Photo sent!")
            except Exception as e:
                await update.message.reply_text(f"Errore nell'inviare la foto: {e}")
                print(f"DEBUG: Exception: {e}")
    else:
        print("DEBUG: update.message is None")
        
         

async def handle_pika(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Pikachu! ⚡")

async def webhook_handler(request):
    data = await request.json()
    update = Update.de_json(data, app.bot)
    await app.update_queue.put(update)
    return web.Response()

async def on_startup(app_):
    webhook_url = f"{APP_URL}/webhook"
    print(f"Setting webhook to: {webhook_url}")
    await app.bot.set_webhook(webhook_url)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("pika", handle_pika))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_buongiorno))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_bro))

web_app = web.Application()
web_app.add_routes([web.post("/webhook", webhook_handler)])
web_app.on_startup.append(on_startup)

runner = web.AppRunner(web_app)

async def main():
    await app.initialize()
    await app.start()
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", int(os.environ.get("PORT", 10000)))
    await site.start()
    print("Bot pronto. In ascolto su /webhook")
    await asyncio.Event().wait()

if __name__ == '__main__':
    asyncio.run(main())
