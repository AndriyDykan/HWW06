import datetime
import random
import sqlite3

from faker import Faker

GROUPS = ['MTP11', 'MTP12', 'MTP13', 'MTP14', 'MTP15', 'MTP16']
TEACHERS = [Faker().name() for i in range(11)]
SUBJECTS = ['math', 'art', 'science', 'history', 'music', 'geography', 'P.E (Physical Education)', 'drama']


def create_db():
    with open('init_hw06.sql', 'r') as f:
        sql = f.read()

    with sqlite3.connect('hw06.db') as con:
        cur = con.cursor()
        cur.executescript(sql)



def populate_db():
    users_sql_command = "\n".join(
        f"INSERT INTO students (name,group_name) VALUES ('{Faker().name()}','{random.choice(GROUPS)}');" for _ in
        range(10))

    with sqlite3.connect('hw06.db') as con:
        cur = con.cursor()
        cur.executescript(users_sql_command)
        cur.execute("SELECT id from students;")
        user_ids = [obj[0] for obj in cur.fetchall()]

    users_sql_command = "\n".join(
        f"INSERT INTO teachers (tc_name,subject_way) VALUES ('{Faker().name()}','{random.choice(SUBJECTS)}');" for _ in
        range(10))

    with sqlite3.connect('hw06.db') as con:
        cur = con.cursor()
        cur.executescript(users_sql_command)
        cur.execute("SELECT id,subject_way from teachers;")
        teachers_ids = [obj for obj in cur.fetchall()]



    tasks_sql_command = "\n".join(
        f"INSERT INTO subjects (sb_name, mark, teacher,time_of_mark,owner_id) VALUES ('{random.choice(teachers_ids)[1]}', {random.randrange(0, 10)},'{random.choice(teachers_ids)[0]}','time{datetime.datetime.now()}', {random.choice(user_ids)});"
        for i in range(40))
    print(tasks_sql_command)
    with sqlite3.connect('hw06.db') as con:
        cur = con.cursor()
        cur.executescript(tasks_sql_command)


def check_db():
    with sqlite3.connect('hw06.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * from students;")
        result = cur.fetchall()
    print(result)

    with sqlite3.connect('hw06.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * from subjects;")
        result = cur.fetchall()
    print(result)
    with sqlite3.connect('hw06.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * from teachers;")
        result = cur.fetchall()
    print(result)


def select(table_name: str, condition=None):
    if condition is not None:
        querry = f"SELECT * FROM {table_name} WHERE {condition};"
    else:
        querry = f"SELECT * FROM {table_name};"

    with sqlite3.connect('hw06.db') as con:
        cur = con.cursor()
        cur.execute(querry)
        result = cur.fetchall()
    return result


def delete(table_name: str, condition=None):
    if condition is not None:
        querry = f"DELETE  FROM {table_name} WHERE {condition};"
    else:
        querry = f"DELETE  FROM {table_name};"

    with sqlite3.connect('hw06.db') as con:
        cur = con.cursor()
        cur.execute(querry)
        con.commit()


def update(table_name: str, set_condition: str, condition=None):
    querry = f'UPDATE {table_name} SET {set_condition}  WHERE {condition};'
    print(querry)
    with sqlite3.connect('hw06.db') as con:
        cur = con.cursor()
        cur.execute(querry)
        con.commit()


def init_db():
    create_db()
    populate_db()
    check_db()


init_db()
