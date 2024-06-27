from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def generate_get_news_buttons():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    get_stars_btn = KeyboardButton(text="ЗВЕЗДНЫЕ ПАРЫ🌟")
    get_scandals_btn = KeyboardButton(text="СКАНДАЛЫ💔")
    get_premieres_btn = KeyboardButton(text="ПРЕМЬЕРЫ🎬")
    get_people_btn = KeyboardButton(text="ЛЮДИ🤹‍♂️")
    get_fashion_btn = KeyboardButton(text="КРАСОТА И МОДА👠")

    markup.add(get_stars_btn, get_scandals_btn, get_premieres_btn,
               get_people_btn, get_fashion_btn)

    return markup
