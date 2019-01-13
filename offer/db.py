import sqlite3
import os

conn = sqlite3.connect('pythonsqlite.db')
c = conn.cursor()

def creat_table():

    c.execute('''CREATE TABLE IF NOT EXISTS users (id int, username text, password text) ''')


def insert_db_form(index, _username, _password):
    
    c.execute("INSERT INTO users VALUES ('%d', '%s', '%s')"%(index, _username, _password))
    conn.commit()

#insert db
def insert_db():

    minh = open('hihi.txt', 'r').readlines()
    for i in range(len(minh)):
        a = minh[i].split('\n')[0].split('\t')
        insert_db_form(int(a[0]), str(a[1]), str(a[2]))


def read_db():
    acc = []
    for row in c.execute('SELECT DISTINCT * FROM users'):
        print(len(row[2]))
        acc.append(row)
    return acc

creat_table()

flag = input("Do you want add data from txt Y/N?: ")
if (flag == 'y' or flag == 'Y'):
    insert_db()
read = input("Do you want to read db Y/N?: ")
if (read == 'y' or read =='Y'):
    read_db()

conn.close()
