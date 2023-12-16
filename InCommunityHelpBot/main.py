

import telebot
#from flask import Flask, request
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, Update
#from telebot.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from telebot.util import quick_markup
from urllib3.util import url
from termcolor import colored

token = 'token'
InCommunityHelpBot = telebot.TeleBot(token)


#app = Flask(__name__)

'''
Вариант постоянного меню внизу окна
'''

# @InCommunityHelpBot.message_handler(commands=['start', 'button'])
# def start_bot(message):
#     start_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\nЧто хотелось бы узнать?"
#     #    InCommunityHelpBot.send_message(message.chat.id, start_mess, parse_mode='html')
#
#     # @InCommunityHelpBot.message_handler(commands=['button'])
#     # def first_choice(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     button1 = types.KeyboardButton("Инфо о храмах")
#     button2 = types.KeyboardButton("Наши адреса")
#     markup.add(button1, button2)
#
#     InCommunityHelpBot.send_message(message.chat.id, start_mess, parse_mode='html', reply_markup=markup)
#
#
# @InCommunityHelpBot.message_handler(content_types='text')
# def message_reply(message):
#     if message.text == "Инфо о храмах":
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         button_ioanpr = types.KeyboardButton("Рождества Иоанна Предтечи на Пресне")
#         button_irina = types.KeyboardButton("Вмц. Ирины на Бауманской")
#         button_flora = types.KeyboardButton("Флора и Лавра")
#         markup.add(button_irina, button_ioanpr)
#         markup.add(button_irina)
#         markup.add(button_flora)
#         InCommunityHelpBot.send_message(message.chat.id, 'Выберите храм', reply_markup=markup)
#     elif message.text == "Наши адреса":
#         InCommunityHelpBot.send_message(message.chat.id, 'Здесь будут наши адреса')
#
#
# @InCommunityHelpBot.message_handler(content_types='text')
# def message_reply(message):
#     if message.text == "Рождества Иоанна Предтечи на Пресне":
#         InCommunityHelpBot.send_message(message.chat.id,
#                                         f"Адрес: м. Краснопресненская, Малый Предтеченский переулок, д. 2 \nНачало богослужений: 09:30 \nСайт: {'url': 'https://ioannpr.ru/raspisanie-bogosluzhenij'}")
#     elif message.text == "Вмц. Ирины на Бауманской":
#         InCommunityHelpBot.send_message(message.chat.id, 'Здесь будут наши адреса')


'''
Вариант с inline-меню
'''
button_church = InlineKeyboardButton(text='Инфо о храмах', callback_data='church')
button_address = InlineKeyboardButton(text='Наши адреса', callback_data='address')
main_keyboard = InlineKeyboardMarkup().add(button_church, button_address)

button_back = InlineKeyboardButton(text='Вернуться', callback_data='back')

button_ch_ioann = InlineKeyboardButton(text='Рождества Иоанна Предтечи на Пресне', callback_data='ioann')
button_ch_irina = InlineKeyboardButton(text='Вмц. Ирины на Бауманской', callback_data='irina')
button_site = InlineKeyboardButton(text='Site', url="https://core.telegram.org/bots/api")
keyboard_church = InlineKeyboardMarkup([
    [button_ch_ioann],
    [button_ch_irina],
    [button_back]
])
#keyboard_church = InlineKeyboardMarkup().add(button_ch_ioann, button_ch_irina, button_back)

button_addr_AK = InlineKeyboardButton(text='АК', callback_data='AK_adr')
button_addr_IK = InlineKeyboardButton(text='ИК', callback_data='IK_adr')
keyboard_address = InlineKeyboardMarkup([
    [button_addr_AK], [button_addr_IK],
    [button_back]
])

#
#
# # Pre-assign menu text
# FIRST_MENU = "<b>Menu 1</b>\n\nИнфо по храмам"
# SECOND_MENU = "<b>Menu 2</b>\n\nИнфо по адресам"
#
# # Pre-assign button text
# NEXT_BUTTON = "Храмы"
# BACK_BUTTON = "Наши адреса"
# TUTORIAL_BUTTON = "Назад"
#
# # Build keyboards
# FIRST_MENU_MARKUP = InlineKeyboardMarkup([[
#     InlineKeyboardButton(NEXT_BUTTON, callback_data=NEXT_BUTTON)
# ]])
# SECOND_MENU_MARKUP = InlineKeyboardMarkup([
#     [InlineKeyboardButton(BACK_BUTTON, callback_data=BACK_BUTTON)],
#     [InlineKeyboardButton(TUTORIAL_BUTTON, url="https://core.telegram.org/bots/api")]
# ])

@InCommunityHelpBot.message_handler(commands=['start'])
def start_bot(message):
    start_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\nЧто хотелось бы узнать?"

    # markup = types.InlineKeyboardMarkup()
    # button_church = types.InlineKeyboardButton(text='Инфо о храмах', callback_data='church')
    # button_address = types.InlineKeyboardButton(text='Наши адреса', callback_data='address')
    # markup.add(button_church, button_address)

    InCommunityHelpBot.send_message(message.chat.id, start_mess, parse_mode='html', reply_markup=main_keyboard)


# @InCommunityHelpBot.message_handler(commands=['button'])
# def first_bot(message):
#
#     if message.callback_data == "church":
#         church_mess = f"Адреса храмов \nПройти"
#
#         markup = types.InlineKeyboardMarkup()
#         button_ioann = types.InlineKeyboardButton(text='Рождества Иоанна Предтечи на Пресне', callback_data='ioann')
#         button_irina = types.InlineKeyboardButton(text='Вмц. Ирины', callback_data='irina')
#         markup.add(button_ioann)
#         markup.add(button_irina)
#
#         InCommunityHelpBot.send_message(message.chat.id, church_mess, parse_mode='html', reply_markup=markup)
#
@InCommunityHelpBot.callback_query_handler(func=lambda call: True)
def response_first(call):
    if call.message:
        if call.data == "church":
            second_mess = "Информация по храмам"
            # markup = types.InlineKeyboardMarkup()
            # button_ioann = types.InlineKeyboardButton(text='Рождества Иоанна Предтечи на Пресне', callback_data='ioann')
            # button_irina = types.InlineKeyboardButton(text='Вмц. Ирины на Бауманской', callback_data='irina')
            # markup.add(button_ioann)
            # markup.add(button_irina)
            #
            # InCommunityHelpBot.send_message(call.message.chat.id, second_mess, parse_mode='html', reply_markup=markup)

            # markup = quick_markup({
            #     'Рождества Иоанна Предтечи на Пресне': {'url': 'https://ioannpr.ru/raspisanie-bogosluzhenij'},
            #     'Вмц. Ирины на Бауманской': {'url': 'http://храм-ирины.рф/расписание-богослужений/'},
            #     'Back': {'callback_data': 'church'},
            #     'Инфо': {'callback_data': 'Инфо о храмах'},
            #     'Inline_query': {'switch_inline_query_current_chat': '???'}
            # }, row_width=1)
            InCommunityHelpBot.send_message(call.message.chat.id, second_mess, reply_markup=keyboard_church)

        elif call.data == "address":
            address_mess = "Информация по адресам"
            InCommunityHelpBot.send_message(call.message.chat.id, address_mess, parse_mode='html', reply_markup=keyboard_address)

        if call.data == 'ioann':
            ioann_info = f"<u>Храм Рождества Иоанна Предтечи</u>\n\n" \
                         f"<b><i>Адрес:</i></b> м. Краснопресненская, Малый Предтеченский переулок, д. 2 \n" \
                         f"<b><i>Начало богослужений:</i></b> 09:30 \n" \
                         f"<b><i>Сайт:</i></b> https://ioannpr.ru/raspisanie-bogosluzhenij"
            InCommunityHelpBot.send_message(call.message.chat.id, ioann_info, parse_mode='html')
        elif call.data == 'irina':
            irina_info = f"Храм вмц. Ирины\n\n" \
                         f"<b><i>Адрес:</i></b> м. Бауманская,..., д. 2. \n" \
                         f"<b><i>Начало богослужений:</i></b> 10:00 \n" \
                         f"<b><i>Сайт:</i></b> http://храм-ирины.рф/расписание-богослужений/"
            InCommunityHelpBot.send_message(call.message.chat.id, irina_info, parse_mode='html')

        if call.data == 'AK_adr':
            AK_info = f"Адрес: м. Рассказовка, бульвар Андрея Тарковского, д.4, кв.429, 7 подъезд, д/ф 429, 3 эт.\n\n" \
                      f"Как добраться: 1 вагон из центра. Если на автобусе, то налево, 50 м до ост. Авт 333, 3-я остановка\n" \
                      f"Если пешком: выход из метро направо, далее - прямо и прямо вдоль дороги метров 500 до светофора. На светофоре налево будет входная группа.\n Для прохода нужен пропуск"
            InCommunityHelpBot.send_message(call.message.chat.id, AK_info, parse_mode='html')
#
# # @InCommunityHelpBot.callback_query_handler(func=lambda call: True)s
# def response_second(call):
#     if call.message:
#         if call.data == "ioann":
#             ioann_mess = "Адрес: м. Краснопресненская, Малый Предтеченский переулок, д. 2."
#             InCommunityHelpBot.send_message(call.message.chat.id, ioann_mess, parse_mode='html')
#
#         elif call.data == "irina":
#             irina_mess = "Адрес: м. Бауманская,..., д. 2. Начало богослужений: 10:00 Сайт: 'http://храм-ирины.рф/расписание-богослужений/'"
#             InCommunityHelpBot.send_message(call.message.chat.id, irina_mess, parse_mode='html')

# f"Адрес: м. Краснопресненская, Малый Предтеченский переулок, д. 2 "
# f"\nНачало богослужений: 09:30 "
# f"\nСайт: 'https://ioannpr.ru/raspisanie-bogosluzhenij'"

if __name__ == '__main__':
    InCommunityHelpBot.polling(none_stop=True)
    #InCommunityHelpBot.infinity_polling()


# @app.route("/" + token, methods=['POST'])
# def getMessage():
#     InCommunityHelpBot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
#     return "!", 200
#
#
# InCommunityHelpBot.remove_webhook()
# InCommunityHelpBot.set_webhook('https://test.com/' + token)
# app.run()run
