import os
import telebot
from googletrans import Translator
translator = Translator()

bot = telebot.TeleBot(os.environ.get('TOKEN'))

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет, вводи любые слова на русском, а я буду переводить их на английский. Только учти, я ещё учусь :)")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, translator.translate(message.text, dest='en').text)

bot.infinity_polling()
