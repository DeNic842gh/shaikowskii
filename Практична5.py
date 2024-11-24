import telebot

TOKEN = '7906404044:AAGxI5riFUMwoLHmd9iD-OMZ2Rt3Uwz7C50'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)

def echo_message(message):
    bot.reply_to(message, message.text)

bot.polling()
