from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8752669113:AAFRiRJUhKn9KkEB3tPT_h7VCmCFkcls9LU"

app = Flask(__name__)

# ساخت اپ تلگرام
application = ApplicationBuilder().token(TOKEN).build()

# هندلر تست
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ربات فعاله ✅")

application.add_handler(CommandHandler("start", start))

# مسیر webhook
@app.route(f"/{TOKEN}", methods=["POST"])
async def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, application.bot)
    await application.process_update(update)
    return "ok"

# اجرای سرور
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
