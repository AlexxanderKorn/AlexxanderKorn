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
    sorted_dict = dict(sorted(bot_buttons.items(), key=lambda x: x[1]))
    menu_buttons = []

    for key in sorted_dict.keys():
        key = InlineKeyboardButton(text=sorted_dict[key], callback_data=key)
        menu_buttons.append(key)

    return list(bot_buttons), menu_buttons


def ch_data_set(ch_d: str):
    ch_data = (database.ch_info(ch_d)[0])

    ch_set = (
        f'<u><b>Храм:</b></u>    {ch_data[1]}\n'
        f'<b>Настоятель:</b><i> {ch_data[12], ch_data[13]}</i>\n\n'
        f'<u><b>Адрес:</b></u><i>   {ch_data[2]}</i>\n'
        f'<b>Как добраться:</b><i> {ch_data[3]}</i>\n\n'
        f'<b>Начало богослужений:</b><i> {ch_data[6]}</i>\n'
        f'<b>Сайт:</b><i>    {ch_data[5]}</i>')
    return ch_set


def people_data_set(people_d: str):
    p_data = (database.people_info(people_d)[0])
    p_car = f'<b>Авто:</b><i>    {p_data[10]}  {p_data[11]}</i>' if (p_data[7]) != 0 else ''
    contact = f'<i>(@{p_data[4]})</i>' if p_data[4] else ''
    comment = f'<b>!!!:</b><i>    {p_data[8]}</i>' if p_data[8] else ''

    p_set = (
        f'<b>{p_data[2]}</b> {contact}\n\n'
        f'<u><b>Адрес:</b></u><i>   {p_data[3]}</i>\n\n'
        f'<b>Как добраться:</b><i> {p_data[5]}</i>\n\n'
        f'{comment}\n'
        f'{p_car}'
    )
    return p_set


button_church = InlineKeyboardButton(text='Инфо о храмах', callback_data='church')
button_address = InlineKeyboardButton(text='Наши адреса', callback_data='address')
main_keyboard = InlineKeyboardMarkup().add(button_church, button_address)

button_back = InlineKeyboardButton(text='Вернуться', callback_data='back')
keyboard_back = InlineKeyboardMarkup([[button_back]])


@InCommunityHelpBot.message_handler(commands=['start'])
def start_bot(message):
    user_name = message.from_user.username
    user_full_name = f"{message.from_user.first_name}" if (message.from_user.first_name and message.from_user.last_name) else user_name
    start_mess = f"<b>{user_full_name}</b>, привет!\nЧто хотелось бы узнать?"

    InCommunityHelpBot.send_message(message.chat.id, start_mess, parse_mode='html', reply_markup=main_keyboard)
    # return user_name


@InCommunityHelpBot.callback_query_handler(func=lambda call: True)
def bot_interaction(call):
    info_ch_menu = bot_buttons_set('ch')
    ch_d = info_ch_menu[0]
    info_ch_keyboard = InlineKeyboardMarkup([info_ch_menu[1]])

    info_people_menu = bot_buttons_set('people')
    people_d = info_people_menu[0]
    info_people_keyboard = InlineKeyboardMarkup([info_people_menu[1]])

    if call.message:
        if call.data == "church":
            second_mess = "Информация по храмам"

            InCommunityHelpBot.send_message(call.message.chat.id,
                                            second_mess,
                                            parse_mode='html',
                                            reply_markup=info_ch_keyboard)

        elif call.data == "address":
            address_mess = "Информация по адресам"
            InCommunityHelpBot.send_message(call.message.chat.id,
                                            address_mess,
                                            parse_mode='html',
                                            reply_markup=info_people_keyboard)
            # else:
            #     InCommunityHelpBot.send_message(call.message.chat.id, 'Пока у вас нет прав смотреть адреса', parse_mode='html',
            #                                     reply_markup=main_keyboard)

        if call.data in ch_d:
            InCommunityHelpBot.send_message(call.message.chat.id,
                                            ch_data_set(call.data),
                                            parse_mode='html',
                                            reply_markup=keyboard_back)
        elif call.data in people_d:
            InCommunityHelpBot.send_message(call.message.chat.id,
                                            people_data_set(call.data),
                                            parse_mode='html',
                                            reply_markup=keyboard_back)

        elif call.data == "back":
            init_mess = f'Что хотелось бы узнать?'
            InCommunityHelpBot.send_message(call.message.chat.id, init_mess, parse_mode='html', reply_markup=main_keyboard)


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
# app.run()
