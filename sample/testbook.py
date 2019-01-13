data = {'cothuyanninh':'minhminh', 
		'minhnamhung3g':'minhlinh'}

class Login :
	def __init__(self, username, password):
		self.username = username
		self.password = password

	def check():
		username = input("Username is: ")
		password = input("Password is: ")
		if (username != self.username or password != self.password):
			print("Username or password is not correct !")
		else:
			print("Login success.")

			