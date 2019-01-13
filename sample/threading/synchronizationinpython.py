import time
import threading

class Account:
	def __init__(self, name, accountTotal):
		self.accountTotal =  accountTotal
		self.name = name

def withdraw(account , amount):
	lock.acquire() # lock cai thread nay lai, khong cho thang khac vao
	account.accountTotal = int(account.accountTotal)
	amount = int(amount)
	for i in range(10):
		if account.accountTotal >= amount :
			account.accountTotal -= amount
			print("Balance Amount {0}: {1}".format(account.name, account.accountTotal))
		else :
			print("Account {0} don't enough money to draw!".format(account.name))

		time.sleep(1)
	lock.release() # giai phong cai lock cho thang tiep theo

lock = threading.Lock() # su sung de dong bo
account1 = Account("account1", "20100")
thread1 = threading.Thread(target = withdraw, args = (account1, 1000))
thread2 = threading.Thread(target = withdraw, args = (account1, 2000))
thread1.start()
thread2.start()