from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Ваш токен
TOKEN = "7906404044:AAGxI5riFUMwoLHmd9iD-OMZ2Rt3Uwz7C50"

# Команда /start
async def start(update: Update, context):
    await update.message.reply_text("Привіт! Я бот. Що хочеш зробити?")

# Ехо-відповідь на повідомлення
async def echo(update: Update, context):
    await update.message.reply_text(update.message.text)

# Головна функція
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Бот запущений!")
    app.run_polling()