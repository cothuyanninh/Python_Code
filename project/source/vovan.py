import sqlite3

def taobd2():
	connect = sqlite3.connect('..//data//output//db3.db')
	c = connect.cursor()

	c.execute("DROP TABLE IF EXISTS People;")
	c.execute("CREATE TABLE People(Id int, Name TEXT, Age int, Gender TEXT)")
	# c.execute("INSERT INTO People(Id, Name) VALUES ("+'1'+"," + str('Minh') +");")
	# c.executemany('INSERT INTO PEOPLE VALUES (?,?,?,?,?)', listDataFromCV)

	connect.commit()

taobd2()