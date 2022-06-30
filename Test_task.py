# Импорт необходимых библиотек
import sqlite3
import os
import requests
import json

# Соединение и проверка БД
conn = sqlite3.connect('questionDB.db')

def check_db(filename):
    return os.path.exists(filename)
# print('База данных на месте')

# Создание курсора для работы с БД и создание нужной таблицы questions
cur = conn.cursor()
# cur.execute("DROP TABLE IF EXISTS questions")
cur.execute("""CREATE TABLE IF NOT EXISTS questions(
   group_id INT,
   group_name TEXT,
   question_id INT,
   question TEXT,
   answer TEXT);
""")
conn.commit()

# Получение данных с jservice.io
s = requests.get('https://jservice.io/api/random')
# Код ответа сервера
#print(s.status_code)

# Получение из состава данных -- значений для полей нашей таблицы
l = s.text
res_dict=json.loads(l)

#print(res_dict)
for x in res_dict:
   qu_id = x.get('id')
   ans = x.get('answer')
   qu = x.get('question')
   gr_id = x.get('category_id')
gr = res_dict[0]['category']
gr_n = gr['title']

# qu_id = res_dict[0]['id']
# ans = res_dict[0]['answer']
# qu = res_dict[0]['question']
# gr_id = res_dict[0]['category_id']
# gr = res_dict[0]['category']
# gr_n = dict()

# print(qu_id, ans, qu, gr_id, gr_n)

# Добавление данных в таблицу questions
val = (gr_id, gr_n, qu_id, qu, ans)
cur.execute("INSERT INTO questions VALUES(?, ?, ?, ?, ?);", val)
conn.commit()

# Выборка данных из БД и вывод на экран. Сортировка по id группы и названию группы вопросов
cur.execute("""SELECT *
    FROM questions
    ORDER BY group_id, question_id
    """)
for row in cur.fetchall():
    group_id, group_name, question_id, question, answer = row
    print(*row, sep=', ')

# Закрытие соединения с БД
conn.close();

