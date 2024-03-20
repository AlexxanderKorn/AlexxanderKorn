import telebot

from keyboa import Keyboa
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from InCommunityHelpBot.db.database import Database

database = Database()


class UsrName:
    """
        Класс для сохранения имени тг-пользователя. Используется для вывода некоторых дополнительных данных
    """
    name = {}


# /Users/aakorneev/PycharmProjects/AlexxanderKorn/InCommunityHelpBot/bot_tok.txt
# /app/InCommunityHelpBot/bot_tok.txt
with open('/app/InCommunityHelpBot/bot_tok.txt') as f:
    token = f.read()

InCommunityHelpBot = telebot.TeleBot(token)


def bot_buttons_set(table: str):
    """Получение названий для кнопок из БД. Наборы кнопок соответствуют значениям полей в задаваемой таблице
    :param table:
        Таблица с информацией об учреждениях или наших адресах
    :return:
        Список названий кнопок и список значений для формирования меню кнопок
    """
    bot_buttons = (database.bot_buttons(table))
    sorted_dict = dict(sorted(bot_buttons.items(), key=lambda x: x[1]))
    menu_buttons = []

    for key in sorted_dict.keys():
        key = InlineKeyboardButton(text=sorted_dict[key], callback_data=key)
        menu_buttons.append(key)

    return list(bot_buttons), menu_buttons


button_church = InlineKeyboardButton(text='Инфо о храмах', callback_data='church')
button_address = InlineKeyboardButton(text='Наши адреса', callback_data='address')
button_other_addr = InlineKeyboardButton(text='Разное', callback_data='other')
main_keyboard = InlineKeyboardMarkup().add(button_church, button_address)

button_back = InlineKeyboardButton(text='Вернуться', callback_data='back')
keyboard_back = InlineKeyboardMarkup([[button_back]])

def p_adm_data_define(user_name):
    """Определение юзера с расширенными возможностями
    :param user_name: 
        тг-контакт
    :return: 
        флаг полномочий
    """
    p_user_select = database.people_adm_info(user_name)
    p_adm_data = (p_user_select[0][1] if p_user_select else '')
    
    return p_adm_data


@InCommunityHelpBot.message_handler(commands=['start'])
def start_bot(message):
    """Приветствие и определение имени тг-контакта. Сохранение тг-контакта для последующего использования
    :param message:
        Данные о пользователе и сообщении
    :return:
        Главное меню
    """

    user_name = message.from_user.username
    UsrName.name['user_name'] = user_name

    user_full_name = f"{message.from_user.first_name}" if message.from_user.first_name else user_name
    start_mess = f"<b>{user_full_name}</b>, привет!\nЧто хотелось бы узнать?"

    p_adm_data = p_adm_data_define(user_name)

    if p_adm_data == 1:
        main_keyboard_shown = InlineKeyboardMarkup().add(button_church, button_address, button_other_addr)
    else:
        main_keyboard_shown = main_keyboard

    InCommunityHelpBot.send_message(message.chat.id, start_mess, parse_mode='html', reply_markup=main_keyboard_shown)


def ch_data_set(ch_d: str):
    """Отформатированная информация по храмам из БД для вывода в боте
    :param ch_d:
        Таблица с храмами
    :return:
        Информация по храмам
    """
    ch_data = (database.ch_info(ch_d)[0])

    ch_set = (
        f'<u><i>Храм:</i></u>    {ch_data[1]}\n'
        f'<i>Настоятель:</i>   {ch_data[12], ch_data[13]}\n\n'
        f'<i>Начало богослужений:</i>   {ch_data[6]}\n\n'
        f'<i>Тел.:</i>    {ch_data[7]}\n'
        f'<i>Сайт:</i>    {ch_data[5]}\n\n'
        f'<u><i>Адрес:</i></u>   {ch_data[2]}\n'
        f'{ch_data[3]}\n(<i>{ch_data[4]}</i>)'
    )
    return ch_set


def people_data_set(people_d: str):
    """Отформатированная информация по адресам из БД для вывода в боте
    :param people_d:
        Таблица с адресами
    :return:
        Информация по адресам
    """
    # Имя тг-пользователя
    usr_name = UsrName.name['user_name']
    # Определение привилегий
    p_adm_data = p_adm_data_define(usr_name)

    p_data = (database.people_info(people_d)[0])

    if p_adm_data == 1 and (p_data[7]) != 0:
        p_car = f'<i>авто:</i>    {p_data[11]}  {p_data[12]}'
    else:
        p_car = ''
    contact = f'<a href="https://t.me/{p_data[4]}">{p_data[2]}</a>'
    route = f'<i>({p_data[6]})</i>' if p_data[6] else ''
    comment = f'<b>!!!</b><i>    {p_data[8]}</i>' if p_data[8] else ''

    p_set = (
        f'<b>{contact}</b>\n\n'
        f'<u><i>Адрес:</i></u>   {p_data[3]}\n\n'
        f'{p_data[5]}\n'  # Как добраться
        f'<i>{route}</i>\n\n'  # Маршрут
        f'{comment}\n\n'  # Особые пометки
        f'{p_car}'
    )
    return p_set


def other_data_set(other_d: str):
    """Отформатированная информация по разным адресам из БД для вывода в боте
    :param other_d:
        Таблица с адресами
    :return:
        Информация по адресам
    """
    other_data = (database.other_info(other_d)[0])
    comm = f'<i>Комментарий:</i>   {other_data[8]}\n\n' if other_data[8] else ''
    phone = f'<i>Тел.:</i>    {other_data[7]}\n\n' if other_data[7] else ''
    w_time = f'<i>Время:</i>   {other_data[6]}\n\n' if other_data[6] else ''
    site = f'<i>Сайт:</i>    {other_data[5]}\n\n' if other_data[5] else ''
    other_set = (
        f'<u><i>Место:</i></u>    {other_data[1]}\n'
        f'{w_time}'
        f'{comm}'
        f'{phone}'
        f'{site}'
        f'<u><i>Адрес:</i></u>   {other_data[2]}\n'
        f'{other_data[3]}\n(<i>{other_data[4]}</i>)'
    )
    return other_set


@InCommunityHelpBot.callback_query_handler(func=lambda call: True)
def bot_interaction(call):
    info_ch_menu = bot_buttons_set('ch')
    ch_d = info_ch_menu[0]
    info_ch_keyboard = Keyboa(items=info_ch_menu[1])

    info_people_menu = bot_buttons_set('people')
    people_d = info_people_menu[0]
    info_people_keyboard = Keyboa(items=info_people_menu[1])  # InlineKeyboardMarkup([info_people_menu[1]])

    info_other_menu = bot_buttons_set('other')
    other_d = info_other_menu[0]
    info_other_keyboard = Keyboa(items=info_other_menu[1])
    
    try:
        usr_name = UsrName.name['user_name']
    except KeyError:
        InCommunityHelpBot.send_message(call.message.chat.id, 'Возникла ошибка. Отправьте сообщение /start',
                                        parse_mode='html')

    if call.message:
        if call.data == "church":
            second_mess = "Информация по храмам"

            InCommunityHelpBot.send_message(call.message.chat.id,
                                            second_mess,
                                            parse_mode='html',
                                            reply_markup=info_ch_keyboard())

        elif call.data == "address":
            p_role_data = p_adm_data_define(usr_name)
            if p_role_data in (0, 1):
                address_mess = "Информация по адресам"
                InCommunityHelpBot.send_message(call.message.chat.id,
                                                address_mess,
                                                parse_mode='html',
                                                reply_markup=info_people_keyboard())
            else:
                InCommunityHelpBot.send_message(call.message.chat.id, 'Пока у вас нет прав смотреть адреса',
                                                parse_mode='html',
                                                reply_markup=keyboard_back)

        elif call.data == "other":
            other_mess = "Информация по разным местам"
            InCommunityHelpBot.send_message(call.message.chat.id,
                                            other_mess,
                                            parse_mode='html',
                                            reply_markup=info_other_keyboard())

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
        elif call.data in other_d:
            InCommunityHelpBot.send_message(call.message.chat.id,
                                            other_data_set(call.data),
                                            parse_mode='html',
                                            reply_markup=keyboard_back)

        elif call.data == "back":
            init_mess = f'Что хотелось бы узнать?'
            # Определение привилегий
            try:
                p_adm_data = p_adm_data_define(usr_name)
            except UnboundLocalError:
                usr_name = UsrName.name['user_name']
                p_adm_data = p_adm_data_define(usr_name)

            if p_adm_data == 1:
                main_keyboard_shown = InlineKeyboardMarkup().add(button_church, button_address, button_other_addr)
            else:
                main_keyboard_shown = main_keyboard

            InCommunityHelpBot.send_message(call.message.chat.id, init_mess, parse_mode='html',
                                            reply_markup=main_keyboard_shown)
