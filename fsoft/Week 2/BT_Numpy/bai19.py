import numpy as np 
import sqlite3
import sys

connection = sqlite3.connect("account.db")
cursor = connection.cursor()
number_of_days = np.random.randint(10000,100000)
lo_of_days = np.random.choice(np.arange(100), 25)
deUnit = 70
loUnit = 4
Cang3Unit = 400

def register(username, name, password):
	cursor.execute("INSERT INTO player (username,name,password,balance) VALUES ('%s','%s','%s','%s');"%(username, name, password,"10000"))
	connection.commit()

def showDb(username, password):
	cursor.execute("SELECT name, username, balance FROM player WHERE username ='%s' and password ='%s'"%(username, password)) 
	result = cursor.fetchall() 
	print("******", len(result))
	for r in result:
		print(r)

def checkAccount(username, password):
	cursor.execute("SELECT * FROM player WHERE username = '%s' and password ='%s'"%(username, password))
	result = cursor.fetchall() 
	if (len(result) != 0):
		return result[0][1] 
	return False

def addMoney(username, amount):
	cursor.execute("SELECT * FROM player WHERE username = '%s'"%username)
	result = cursor.fetchall()
	temp = result[0][3]
	amount_ = temp + amount
	cursor.execute("UPDATE player SET balance = '%s' WHERE username = '%s'"%(amount_, username))
	connection.commit()

def danhDe(username, number, amount):
	cursor.execute("SELECT * FROM player WHERE username = '%s'"%username)
	result = cursor.fetchall()
	temp = result[0][3]
	amount_ = temp - amount
	if (amount_ < 0):
		return False
	if number == int(str(number_of_days)[-2:]):
		print("Congratilation! You are winner!")
		amount_ += amount* deUnit
	else :
		print("You are lose at this turn.")

	cursor.execute("UPDATE player SET balance = '%s' WHERE username = '%s'"%(amount_, username))
	connection.commit()
	return True

def danhLo(username, number, amount):
	cursor.execute("SELECT * FROM player WHERE username = '%s'"%username)
	result = cursor.fetchall()
	temp = result[0][3]
	amount_ = temp - amount
	if (amount_ < 0):
		return False
	if number in lo_of_days:
		print("Congratilation! You are winner!")
		amount_ += amount* loUnit
	else:
		print("You are lose at this turn.")
	cursor.execute("UPDATE player SET balance = '%s' WHERE username = '%s'"%(amount_, username))
	connection.commit()
	return True

def danh3Cang(username, number, amount):
	cursor.execute("SELECT * FROM player WHERE username = '%s'"%username)
	result = cursor.fetchall()
	temp = result[0][3]
	amount_ = temp - amount
	if (amount_ < 0):
		return False
	if number == str(number_of_days)[-3:]:
		print("Congratilation! You are winner!")
		amount_ += amount* Cang3Unit
	else:
		print("You are lose at this turn.")
	cursor.execute("UPDATE player SET balance = '%s' WHERE username = '%s'"%(amount_, username))
	connection.commit()
	return True


if __name__ == "__main__":
	print("XSMB: ", number_of_days)
	true_type = 1
	flag = 1
	choice_after_sign = 1
	endGame = 1
	# showDb()
	while true_type == 1:
		try:
			while True:
				type_sign = int(input("1. Sign up\n2. Sign in\nType your choice : "))
				if type_sign in [1,2]:
					true_type = 0
					break
		except ValueError:
			print("Wrong choice!")

	if type_sign == 1:
		while True:
			try:
				name_user = input("Type your name: ")
				username_user = input("Type your username:  ")
				password_user = input("Type you password: ")
				register(username_user, name_user, password_user)
				break
			except:
				print("This username is not already!")

		type_sign =2
		print("Please Login Again with this Account to Play!")

	

	if type_sign == 2:
		while flag == 1:
			username_user = input("Type your username:  ")
			password_user = input("Type you password: ")
			name_from_db = checkAccount(username_user, password_user)
			if name_from_db != False:
				print("Success, Welcome %s to Bai 19 :v."%(name_from_db))
				flag =0
			else :
				print("Type again, Please!")

	while endGame == 1:
		choice_after_sign = 1
		while choice_after_sign == 1:
			try: 
				type_choice = int(input(("0. Xem thong tin\n1. Nap tien\n2. Danh De\n3. Danh lo\n4. Danh 3 cang\n5. Thoat game\nType your choice: ")))
				if type_choice in [0,1,2,3,4,5]:
					choice_after_sign = 0
			except ValueError:
				print("Type Again!")

		if type_choice == 0:
			showDb(username_user, password_user)

		if type_choice == 1:
			while True:
				try:
					money_ = abs(int(input("Type your money to add: ")))
					break
				except ValueError:
					print("Type again.")
			addMoney(username_user, money_)

		if type_choice == 2:
			flag2 = 1
			while flag2 == 1:
				try:
					number_de = int(input("Type your number to play De: "))
					amount_de = int(input("Type your money to play De: "))
				except ValueError:
					print("Type again.")
					continue
				if danhDe(username_user, number_de, amount_de) == True:
					flag2 = 0
					continue
				else:
					print("You donn't have enough money!")

		if type_choice == 3:
			flag3 = 1
			while flag3 == 1:
				try:
					number_lo = int(input("Type your number to play Lo: "))
					amount_lo = int(input("Type your money to play Lo: "))
				except ValueError:
					print("Type again.")
					continue
				if danhDe(username_user, number_lo, amount_lo) == True:
					flag3 = 0
					continue
				else:
					print("You donn't have enough money!")

		if type_choice == 4:
			flag4 = 1
			while flag4 == 1:
				try:
					number_3cang = int(input("Type your number to play 3 cang: "))
					amount_3cang = int(input("Type your money to play 3 cang: "))
				except ValueError:
					print("Type again.")
					continue
				if danhDe(username_user, number_3cang, amount_3cang) == True:
					flag3 = 0
					continue
				else:
					print("You donn't have enough money!")

		if type_choice == 5:
			print("See you soon!")
			sys.exit()
				





		#showDb()

cursor.close()
connection.close()