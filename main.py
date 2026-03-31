from fastapi import FastAPI, Request
from dotenv import load_dotenv
from telegram import Bot, Update
from contextlib import asynccontextmanager
from logger import logger
import os
from langchain.chat_models import init_chat_model
from pprint import pformat
import json
load_dotenv()

llm = init_chat_model(model="gpt-5-mini", model_provider="openai")
bot = Bot(token=os.getenv("BOT_TOKEN"))

WEBHOOK_URL = os.getenv("WEBHOOK_URL")

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Server Startup")
    try:
        await bot.set_webhook(url=f"{WEBHOOK_URL}/webhook")
        logger.info("Webhook is set up")
    except Exception:
        logger.error("Cannot Set Up Webhook URL")
    yield
    logger.info("Shutting Down Server")

app = FastAPI(lifespan=lifespan)


@app.post("/webhook")
async def handle_webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, bot)

    if update.message and update.message.text:
        logger.debug(f"Here's the message object:\n%s", json.dumps(update.to_dict(), indent=3, default=str))
        
        await bot.send_message(chat_id=update.message.chat_id, text="Hey from server")
    return {"results": "ok"}

