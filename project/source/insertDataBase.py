import sqlite3

def insertToDataBaseSecond(listDataFromCV):
	connect = sqlite3.connect('..//data//output//databaseCV.db')
	c = connect.cursor()
	c.executemany('INSERT INTO candidate VALUES (?,?,?,?,?)', listDataFromCV)

	connect.commit()
	
	# for row in c.execute("SELECT * FROM candidate"):
	# 	print(row)


def insertToDataBaseFirst(listDataFromCV):
	connect = sqlite3.connect('..//data//output//databaseCV.db')
	c = connect.cursor()

	c.execute("DROP TABLE IF EXISTS candidate;")
	c.execute("CREATE TABLE candidate(location TEXT, name TEXT, phone TEXT, email TEXT, linkfile TEXT)")
	#c.execute("INSERT INTO candidate VALUES ('1', name1, email1, numberphone1)")
	c.executemany('INSERT INTO candidate VALUES (?,?,?,?,?)', listDataFromCV)

	connect.commit()

def showDatabase():
	connect = sqlite3.connect('..//data//output//databaseCV.db')
	c = connect.cursor()
	for row in c.execute("SELECT * FROM candidate"):
		print(row)

