from telebot import TeleBot

from configs import TOKEN

from keyboards import *

from utils import *

bot = TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def cmd_start(message):
    chat_id = message.chat.id

    bot.send_message(chat_id,
                     "Привет!👋🏻")


@bot.message_handler(commands=['help'])
def cmd_help(message):
    chat_id = message.chat.id

    bot.send_message(chat_id,
                     f"""Я бот, который отправляет вам новости😊                    
Вам нужно выбрать одну из категорий ниже👇🏻""",
                     reply_markup=generate_get_news_buttons())


@bot.message_handler(func=lambda message: message.text == "ЗВЕЗДНЫЕ ПАРЫ🌟")
def send_stars(message):
    chat_id = message.chat.id
    stars_news = generate_normal_text()

    for text, photo in stars_news:
        bot.send_photo(chat_id,
                       photo=photo,
                       caption=text)


@bot.message_handler(func=lambda message: message.text == "СКАНДАЛЫ💔")
def send_stars(message):
    chat_id = message.chat.id
    scandals_news = generate_normal_text_2()

    for text, photo in scandals_news:
        bot.send_photo(chat_id,
                       photo=photo,
                       caption=text)


@bot.message_handler(func=lambda message: message.text == "ПРЕМЬЕРЫ🎬")
def send_stars(message):
    chat_id = message.chat.id
    premieres_news = generate_normal_text_3()

    for text, photo in premieres_news:
        bot.send_photo(chat_id,
                       photo=photo,
                       caption=text)


@bot.message_handler(func=lambda message: message.text == "ЛЮДИ🤹‍♂️")
def send_stars(message):
    chat_id = message.chat.id
    people_news = generate_normal_text_4()

    for text, photo in people_news:
        bot.send_photo(chat_id,
                       photo=photo,
                       caption=text)


@bot.message_handler(func=lambda message: message.text == "КРАСОТА И МОДА👠")
def send_stars(message):
    chat_id = message.chat.id
    fashion_news = generate_normal_text_5()

    for text, photo in fashion_news:
        bot.send_photo(chat_id,
                       photo=photo,
                       caption=text)


bot.polling(none_stop=True)
