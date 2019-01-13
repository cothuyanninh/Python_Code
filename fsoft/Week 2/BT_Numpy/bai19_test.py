import sqlite3

connection = sqlite3.connect("account.db")
cursor = connection.cursor()

sql_command = """
CREATE TABLE IF NOT EXISTS player( 
username VARCHAR(40) PRIMARY KEY, 
name VARCHAR(40), 
password VARCHAR(30),
balance INTEGER) ;"""

cursor.execute(sql_command)

# sql_command1 = "INSERT INTO player (username, name, password, balance) VALUES (%s,%s,%s)"%("'cothuyanninh'","'Minh-chan'","'minhminh'")
# print(sql_command1)
# cursor.execute(sql_command1)

# cursor.execute("SELECT * FROM player")
# result = cursor.fetchall() 
# print(len(result))