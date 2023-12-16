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

create_ch = """
INSERT INTO
  ch (ch_name, ch_address, ch_how_get, ch_navigation, ch_url, ch_prayer_time, ch_comment, abbot_id)
VALUES
  ('Рождества Иоанна Предтечи на Пресне', '', 'male', 'USA'),
  ('Вмц. Ирины на Бауманской', 32, 'female', 'France'),
  ('Флора и Лавра на Павелецкой', 35, 'female', 'England'),
  ('Mike', 40, 'male', 'Denmark'),
  ('Elizabeth', 21, 'female', 'Canada');
"""

create_users = """
INSERT INTO
  users (name, age, gender, nationality)
VALUES
  ('James', 25, 'male', 'USA'),
  ('Leila', 32, 'female', 'France'),
  ('Brigitte', 35, 'female', 'England'),
  ('Mike', 40, 'male', 'Denmark'),
  ('Elizabeth', 21, 'female', 'Canada');
"""

create_posts = """
INSERT INTO
  posts (title, description, user_id)
VALUES
  ("Happy", "I am feeling very happy today", 1),
  ("Hot Weather", "The weather is very hot today", 2),
  ("Help", "I need some help with my work", 2),
  ("Great News", "I am getting married", 1),
  ("Interesting Game", "It was a fantastic game of tennis", 5),
  ("Party", "Anyone up for a late-night party today?", 3);
"""

create_comments = """
INSERT INTO
  comments (text, user_id, post_id)
VALUES
  ('Count me in', 1, 6),
  ('What sort of help?', 5, 3),
  ('Congrats buddy', 2, 4),
  ('I was rooting for Nadal though', 4, 5),
  ('Help with your thesis?', 2, 3),
  ('Many congratulations', 5, 4);
"""

create_likes = """
INSERT INTO
  likes (user_id, post_id)
VALUES
  (1, 6),
  (2, 3),
  (1, 5),
  (5, 4),
  (2, 4),
  (4, 2),
  (3, 6);
"""

select_users = "SELECT * FROM users"

connection = create_connection("/Users/aakorneev/Projects/Test/sm_app.sqlite")

query_execute(connection, create_table_users)
query_execute(connection, create_table_posts)
query_execute(connection, create_table_comments)
query_execute(connection, create_table_likes)

query_execute(connection, create_users)
query_execute(connection, create_posts)
query_execute(connection, create_comments)
query_execute(connection, create_likes)

users = execute_read_query(connection, select_users)
for user in users:
    print(user)

select_posts = "SELECT * FROM posts"
posts = execute_read_query(connection, select_posts)

select_users_posts = """
SELECT
  users.id,
  users.name,
  posts.description
FROM
  posts
  INNER JOIN users ON users.id = posts.user_id
"""

users_posts = execute_read_query(connection, select_users_posts)

for users_post in users_posts:
    print(users_post)

select_posts_comments_users = """
SELECT
  posts.description as post,
  text as comment,
  name
FROM
  posts
  INNER JOIN comments ON posts.id = comments.post_id
  INNER JOIN users ON users.id = comments.user_id
"""

posts_comments_users = execute_read_query(
    connection, select_posts_comments_users
)

for posts_comments_user in posts_comments_users:
    print(posts_comments_user)

