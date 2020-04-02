# Avtor: Mel'nikov Denis :-)))

import COVID19Py
from telebot import types
import telebot

covid = COVID19Py.COVID19()
bot = telebot.TeleBot('1077906522:AAFIfrGr5OxSiRAhc4mnrSZHYrc5Gkuh4LU')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton("🇰🇿 Казахстан")
    btn2 = types.KeyboardButton("🇺🇦 Украина")
    btn3 = types.KeyboardButton("🇧🇾 Беларусь")
    btn4 = types.KeyboardButton("🇷🇺 Россия")
    btn5 = types.KeyboardButton("🇮🇹 Италия")
    btn6 = types.KeyboardButton("🇪🇸 Испания")
    btn7 = types.KeyboardButton("🇨🇳 Китай")
    btn8 = types.KeyboardButton("🇺🇸 США")
    btn9 = types.KeyboardButton("🌎 Мир")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)

    send_mess = f"<b>Привет {message.from_user.first_name}!</b>\nВыберите страну"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "🇰🇿 казахстан":
        location = covid.getLocationByCountryCode("KZ")
    elif get_message_bot == "🇺🇦 украина":
        location = covid.getLocationByCountryCode("UA")
    elif get_message_bot == "🇧🇾 беларусь":
        location = covid.getLocationByCountryCode("BY")
    elif get_message_bot == "🇷🇺 россия":
        location = covid.getLocationByCountryCode("RU")
    elif get_message_bot == "🇮🇹 италия":
        location = covid.getLocationByCountryCode("IT")
    elif get_message_bot == "🇪🇸 испания":
        location = covid.getLocationByCountryCode("ES")
    elif get_message_bot == "🇨🇳 китай":
        location = covid.getLocationByCountryCode("CN")
    elif get_message_bot == "🇺🇸 сша":
        location = covid.getLocationByCountryCode("US")
    else:
        location = covid.getLatest()
        final_message = (f"<b>Данные по миру:</b>\n<b>Заболевшие:</b>{location['confirmed']:,}\n"
                         f"<b>Смертей:</b>{location['deaths']:,}")

    if final_message == "":
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = (f"Население: {location[0]['country_population']:,}\n"
                         f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>"
                         f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Смертей:</b>"
                         f"{location[0]['latest']['deaths']:,}\n")
        # f"<b>Выздоровлено:</b>{location[0]['latest']['recovered']:}")

    bot.send_message(message.chat.id, final_message, parse_mode='html')


bot.polling(none_stop=True)
