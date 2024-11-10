import telebot

API_KEY = '7728599275:AAG1Mhs_UP2RI8eM0cTQKremsH_NLDzXhyg'

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start', 'main', 'hello'])

def main(message):
    bot.send_message(message.chat.id, 'Hello!')

@bot.message_handler(commands=['help'])

def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')

bot.infinity_polling()