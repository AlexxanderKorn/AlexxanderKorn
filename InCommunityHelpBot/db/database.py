import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path, check_same_thread=False)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except Error as e:
        print(f"The error '{e}' has occurred")
    return result


# /Users/aakorneev/PycharmProjects/AlexxanderKorn/InCommunityHelpBot/db_conn.txt
# /app/InCommunityHelpBot/db_conn.txt

# /Users/aakorneev/PycharmProjects/AlexxanderKorn/InCommunityHelpBot/db/info_bot.sqlite
# /app/InCommunityHelpBot/db/info_bot.sqlite

with open('/app/InCommunityHelpBot/db_conn.txt') as db_f:
    db_conn = db_f.read()
    connection = create_connection(db_conn)


class Database:
    def __init__(self):
        self.conn = connection
        self.cursor = self.conn.cursor()

    def people_adm_info(self, tg_name):
        """Определение пользователей с расширенными возможностями
        :param tg_name: 
            тг-контакт
        :return: 
            словарь "контакт, привилег"
        """
        select_p_adm = f"""SELECT p_contact, p_adm FROM people
        WHERE p_contact = '{tg_name}'"""
        people_adm = execute_read_query(connection, select_p_adm)

        return people_adm

    def ch_info(self, ch_name):
        select_ch = f"""SELECT * FROM ch JOIN abbots a ON ch.abbot_id = a.id
        WHERE ch.ch_id_name = '{ch_name}'"""
        ch = execute_read_query(connection, select_ch)

        return ch

    def people_info(self, p_name):
        select_p = f"""SELECT * FROM people p JOIN cars c ON p.car_id = c.id
        WHERE p.p_id_name = '{p_name}'"""
        people = execute_read_query(connection, select_p)

        return people

    def other_info(self, other_name):
        select_other = f"""SELECT * FROM other WHERE oth_id_name = '{other_name}'"""
        other = execute_read_query(connection, select_other)

        return other

    def bot_buttons(self, table):
        rec_count = execute_read_query(connection, f"""SELECT COUNT(*) FROM '{table}'""")
        rec_count_formatted = rec_count[0][0]
        buttons_names = {}
        for i in range(rec_count_formatted):
            i = i + 1
            if table == 'ch':
                tab_values = execute_read_query(connection,
                                                f"""SELECT ch_id_name, ch_name FROM ch WHERE id = '{i}'""")[0]
            elif table == 'people':
                tab_values = execute_read_query(connection,
                                                f"""SELECT p_id_name, p_name FROM people WHERE id = '{i}'""")[0]
            elif table == 'other':
                tab_values = execute_read_query(connection,
                                                f"""SELECT oth_id_name, oth_name FROM other WHERE id = '{i}'""")[0]
            else:
                raise ValueError(f'Table {table} is not defined')
            buttons_names.update({tab_values[0]: tab_values[1]})

        return buttons_names
