from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8752669113:AAFRiRJUhKn9KkEB3tPT_h7VCmCFkcls9LU"

# دیتای تستی (بعدا حرفه‌ای می‌کنیم)
secret_data = {
    1: {
        "target": 907489298,  # اینجا user_id خودتو بذار
        "text": "این یک پیام محرمانه است 🔐"
    }
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("👁 مشاهده پیام", callback_data="view_1")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("روی دکمه بزن:", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    data = secret_data[1]

    if user_id == data["target"]:
        await query.answer(data["text"], show_alert=True)
    else:
        await query.answer("❌ دسترسی نداری", show_alert=True)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()
print(update.message.from_user.id)
