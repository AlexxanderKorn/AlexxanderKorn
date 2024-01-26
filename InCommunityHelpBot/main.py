import telebot
# from flask import Flask, request
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, Update
# from telebot.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from telebot.util import quick_markup
from urllib3.util import url
# from termcolor import colored
from database import Database

"""
    . Запуск бота: python <имя py-файла>
    . Данные содержатся в БД
"""

database = Database()

with open('/Users/aakorneev/PycharmProjects/AlexxanderKorn/InCommunityHelpBot/bot_tok.txt') as f:
    token = f.read()

InCommunityHelpBot = telebot.TeleBot(token)


# app = Flask(__name__)

def out_yellow(text):
    pp = "\033[33m {}".format(text)

    return pp


def bot_buttons_set(table: str):
    bot_buttons = (database.bot_buttons(table))
    menu_buttons = []

    for key in bot_buttons.keys():
        key = InlineKeyboardButton(text=bot_buttons[key], callback_data=key)
        menu_buttons.append(key)

    return list(bot_buttons), menu_buttons


def ch_data_set(ch_d: str):
    ch_data = (database.ch_info(ch_d)[0])
    # pr_start = out_yellow("Начало богослужений:")
    ch_set = (
        f'<u><b>Храм:</b></u>    {ch_data[1]}\n'
        f'<b>Настоятель:</b><i> {ch_data[12], ch_data[13]}</i>\n\n'

        f'<u><b>Адрес:</b></u><i>   {ch_data[2]}</i>\n'
        f'<b>Как добраться:</b><i> {ch_data[3]}</i>\n\n'

        f'<b>Начало богослужений:</b><i> {ch_data[6]}</i>\n'
        f'<b>Сайт:</b><i>    {ch_data[5]}</i>')
    return ch_set


button_church = InlineKeyboardButton(text='Инфо о храмах', callback_data='church')
button_address = InlineKeyboardButton(text='Наши адреса', callback_data='address')
main_keyboard = InlineKeyboardMarkup().add(button_church, button_address)

button_back = InlineKeyboardButton(text='Вернуться', callback_data='back')
keyboard_back = InlineKeyboardMarkup([[button_back]])


button_addr_AK = InlineKeyboardButton(text='АК', callback_data='AK_adr')
button_addr_IK = InlineKeyboardButton(text='ИК', callback_data='IK_adr')
button_addr_KB = InlineKeyboardButton(text='КБ', callback_data='KB_adr')
keyboard_address = InlineKeyboardMarkup([
    [button_addr_AK], [button_addr_IK], [button_addr_IK],
    [button_back]
])


@InCommunityHelpBot.message_handler(commands=['start'])
def start_bot(message):
    start_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\nЧто хотелось бы узнать?"

    InCommunityHelpBot.send_message(message.chat.id, start_mess, parse_mode='html', reply_markup=main_keyboard)


@InCommunityHelpBot.callback_query_handler(func=lambda call: True)
def response_first(call):
    info_church_menu = bot_buttons_set('ch')
    ch_d = info_church_menu[0]
    info_keyboard = InlineKeyboardMarkup([info_church_menu[1]])

    if call.message:
        if call.data == "church":
            second_mess = "Информация по храмам"

            InCommunityHelpBot.send_message(call.message.chat.id,
                                            second_mess,
                                            parse_mode='html',
                                            reply_markup=info_keyboard)

        elif call.data == "address":
            address_mess = "Информация по адресам"
            InCommunityHelpBot.send_message(call.message.chat.id,
                                            address_mess,
                                            parse_mode='html',
                                            reply_markup=keyboard_address)

        if call.data in ch_d:
            InCommunityHelpBot.send_message(call.message.chat.id,
                                            ch_data_set(call.data),
                                            parse_mode='html',
                                            reply_markup=keyboard_back)

        elif call.data == "back":
            second_mess = "Информация по храмам"
            InCommunityHelpBot.send_message(call.message.chat.id, second_mess, reply_markup=info_keyboard)

        if call.data == 'AK_adr':
            AK_info = f"Адрес: м. Рассказовка, бульвар Андрея Тарковского, д.4, кв.429, 7 подъезд, д/ф 429, 3 эт.\n\n" \
                      f"Как добраться: 1 вагон из центра. Если на автобусе, то налево, 50 м до ост. Авт 333, 3-я остановка\n" \
                      f"Если пешком: выход из метро направо, далее - прямо и прямо вдоль дороги метров 500 до светофора. На светофоре налево будет входная группа.\n Для прохода нужен пропуск"
            InCommunityHelpBot.send_message(call.message.chat.id, AK_info, parse_mode='html')


if __name__ == '__main__':
    InCommunityHelpBot.polling(none_stop=True)
    # InCommunityHelpBot.infinity_polling()

# @app.route("/" + token, methods=['POST'])
# def getMessage():
#     InCommunityHelpBot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
#     return "!", 200
#
#
# InCommunityHelpBot.remove_webhook()
# InCommunityHelpBot.set_webhook('https://test.com/' + token)
# app.run()run
