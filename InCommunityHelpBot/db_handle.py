import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query was executed successfully")
    except Error as e:
        print(f"The error '{e}' has occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        # return result
    except Error as e:
        print(f"The error '{e}' has occurred")
    return result


def update_table(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Table was updated successfully")
        cursor.close()

    except Error as e:
        print(f"The error '{e}' has occurred")
    finally:
        if connection:
            connection.close()
            print("Connection to SQLite is closed")


# create_table_ch = """
# CREATE TABLE IF NOT EXISTS ch (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   ch_name TEXT NOT NULL,
#   ch_address TEXT,
#   ch_how_get TEXT,
#   ch_navigation BLOB,
#   ch_url TEXT,
#   ch_prayer_time TEXT,
#   ch_phone TEXT,
#   ch_comment TEXT,
#   abbot_id INTEGER,
#   FOREIGN KEY (abbot_id) REFERENCES abbots (id),
#   UNIQUE (id, ch_name)
#
# );
# """
#
# create_table_abbots = """
# CREATE TABLE IF NOT EXISTS abbots (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   abbot_name TEXT NOT NULL,
#   abbot_rank TEXT
# );
# """
#
# create_table_people = """
# CREATE TABLE IF NOT EXISTS people (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   p_id_name TEXT NOT NULL,
#   p_name TEXT NOT NULL,
#   p_address TEXT,
#   p_phone TEXT,
#   p_how_get TEXT,
#   p_navigation BLOB,
#   car_id INTEGER,
#   ch_comment TEXT,
#   FOREIGN KEY (car_id) REFERENCES cars (id),
#   UNIQUE (id, p_id_name)
# );
# """
#
# create_table_cars = """
# CREATE TABLE IF NOT EXISTS cars (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   car_model TEXT NOT NULL,
#   car_number TEXT
# );
# """


connection = create_connection("/Users/aakorneev/PycharmProjects/AlexxanderKorn/InCommunityHelpBot/info_bot.sqlite")

# execute_query(connection, create_table_people)
# execute_query(connection, create_table_cars)

# execute_query(connection, insert_ch)
# execute_query(connection, insert_abb)

# execute_query(connection, update_table_ch)
# execute_query(connection, update_table_abbot)

# select_ch = "SELECT * FROM ch JOIN abbots ON ch.abbot_id = abbots.id;"
# select_abbot = "SELECT * FROM abbots;"

# ch = execute_read_query(connection, select_ch)
# for i in ch:
#     print(i)

# abbot = execute_read_query(connection, select_abbot)
# for i in abbot:
#     print(i)
