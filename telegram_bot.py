print("hkbhjb")
import os
from dotenv import load_dotenv
from telegram.ext import Application, MessageHandler, filters
from agent import tel_agent

load_dotenv()
TELEGRAM_TOKEN = ""
async def reply(update, context):
    result = await tel_agent.ainvoke(
        {"messages": [{"role": "user", "content": update.message.text}]}
        # config = {"configurable":{"thread_id":str(update.effective_chat.id)}}
    )

    await update.message.reply_text(result["messages"][-1].content[0]['text'])

app = Application.builder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, reply))
app.run_polling()