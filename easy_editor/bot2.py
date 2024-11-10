import telebot

API_TOKEN = '7795877895:AAGIDmmmpYNJCtZzLK2I-3vhSddl0MRQ8QQ'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(lambda message: True)
def echo_all(message):
  bot.reply_to(message, message.text)

bot.infinity_polling()