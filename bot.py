""" Telegram Translate Bot """

import os
import telebot
from googletrans import Translator
translator = Translator()

# bot = telebot.TeleBot(os.environ.get('TOKEN'))

@bot.message_handler(commands=['start', 'help'])

def send_welcome(message):
    """ Welcome message for new users """
    bot.reply_to(message, "Привет! Я junior-переводчик с русского на английский. Попробуй :)")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """ Translate users messages """
    bot.reply_to(message, translator.translate(message.text, dest='en').text)

bot.infinity_polling()
