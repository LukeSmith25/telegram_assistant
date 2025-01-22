from fastapi import FastAPI, Request
from telegram import Update, Bot
from telegram.ext import Application
from config import BOT_TOKEN

app = FastAPI()
bot = Bot(token=BOT_TOKEN)

telegram_app = Application.builder().token(BOT_TOKEN).build()

@app.post("/webhook")
async def webhook(request: Request):
    update = Update.de_json(await request.json(), bot)
    await telegram_app.process_update(update)
    return {"status": "ok"}
