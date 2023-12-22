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


def query_execute(connection, query):
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


#
# create_table_users = """
# CREATE TABLE IF NOT EXISTS users (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT NOT NULL,
#   age INTEGER,
#   gender TEXT,
#   nationality TEXT
# );
# """
#
#
# create_table_posts = """
# CREATE TABLE IF NOT EXISTS posts(
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   title TEXT NOT NULL,
#   description TEXT NOT NULL,
#   user_id INTEGER NOT NULL,
#   FOREIGN KEY (user_id) REFERENCES users (id)
# );
# """
#
# create_table_comments = """
# CREATE TABLE IF NOT EXISTS comments (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   text TEXT NOT NULL,
#   user_id INTEGER NOT NULL,
#   post_id INTEGER NOT NULL,
#   FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
# );
# """
#
# create_table_likes = """
# CREATE TABLE IF NOT EXISTS likes (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   user_id INTEGER NOT NULL,
#   post_id integer NOT NULL,
#   FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
# );
# """


create_table_ch = """
CREATE TABLE IF NOT EXISTS ch (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ch_name TEXT NOT NULL,
  ch_address TEXT,
  ch_how_get TEXT,
  ch_navigation BLOB,
  ch_url TEXT,
  ch_prayer_time TEXT,
  ch_phone TEXT,
  ch_comment TEXT,
  abbot_id INTEGER,
  FOREIGN KEY (abbot_id) REFERENCES abbots (id),
  UNIQUE (id, ch_name)

);
"""

create_table_abbots = """
CREATE TABLE IF NOT EXISTS abbots (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  abbot_name TEXT NOT NULL,
  abbot_rank TEXT
);
"""

create_table_people = """
CREATE TABLE IF NOT EXISTS people (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  p_abbr TEXT NOT NULL,
  p_address TEXT,
  p_how_get TEXT,
  p_navigation BLOB,
  car_id INTEGER,
  ch_comment TEXT,
  FOREIGN KEY (car_id) REFERENCES cars (id),
  UNIQUE (id, p_abbr)
);
"""

create_table_cars = """
CREATE TABLE IF NOT EXISTS cars (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  car_model TEXT NOT NULL,
  car_number TEXT
);
"""

# insert_ch = """
# INSERT INTO
#   ch (ch_name, ch_address, ch_how_get, ch_navigation, ch_url, ch_prayer_time, ch_phone, ch_comment, abbot_id)
# VALUES
#   ('Рождества Иоанна Предтечи на Пресне', 'м. Краснопресненская, Малый Предтеченский переулок, д. 2', 'Выход 1 из метро',
#   '/Users/aakorneev/Documents/AK/Bot/IoannPr_how_to_get.jpg',
#   'https://ioannpr.ru/raspisanie-bogosluzhenij', '09:30', '+7-499-255-65-72', '', 1);
# """

# insert_abb = """
# INSERT INTO
#   abbots (abbot_name, abbot_rank)
# VALUES
#   ('Антоний (Севрюк)', 'митр. ');
# """

select_ch = "SELECT * FROM ch JOIN abbots ON ch.abbot_id = abbots.id;"
select_abbot = "SELECT * FROM abbots;"

connection = create_connection("/Users/aakorneev/PycharmProjects/AlexxanderKorn/InCommunityHelpBot/info_bot.sqlite")

# query_execute(connection, create_table_ch)
# query_execute(connection, create_table_abbots)

# query_execute(connection, insert_ch)
# query_execute(connection, insert_abb)

ch = execute_read_query(connection, select_ch)
for i in ch:
    print(i)

# abbot = execute_read_query(connection, select_abbot)
# for i in abbot:
#     print(i)

