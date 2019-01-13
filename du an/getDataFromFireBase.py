from firebase import firebase
import logic


price_init = 300
firebase_post = firebase.FirebaseApplication('https://last-firebase-ea3d3.firebaseio.com/customers', None)
firebase = firebase.FirebaseApplication('https://project-winter-2018.firebaseio.com', None)

class Firebase():

	def __init__(self, name, timeFinish, uid, price):

		self.name = name
		# self.numberOfPrint = int(numberOfPrint)
		# self.page = int(page)
		self.timeFinish = timeFinish
		self.uid = uid
		# self.url = url
		self.price = price


	def postToFirebase(self):

		dict_post = {'uid': self.uid, 'timeFinish': self.timeFinish, 'name': self.name, 'price': self.price}
		result = firebase_post.post("/customers", dict_post)
		return result


def countMoney(page, numberOfPrint, price):

	return int(page)*int(numberOfPrint)*int(price)


def getToFirebase():

	data = firebase.get('/customers', None)
	# list_key = list(data.keys())

	return data
	# list_time = []
	# for i in range(len(list_key)):
	# 	a = data[list_key[i]]
	# 	b = countMoney(a['page'],a['numberOfPrint'],price_init)
	# 	time = logic.converTime(a['timeFinish']).isoformat()

	# 	Firebase(uid = a['uid'], timeFinish = a['timeFinish'], price = b, name = a['name'] ).postToFirebase()
	# 	list_time.append((a['uid'], a[timeFinish]))



# Firebase(uid = "Az09kL", timeFinish = "22-11-2011", page = "20", numberOfPrint = '5', name = "Hong lau mong", url = "https://vi.wikipedia.org/logo.svg").postToFirebase()
# getToFirebase()