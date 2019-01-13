import threading
import time

class myThread(threading.Thread):
	def __init__(self, name, counter, delayTime):
		threading.Thread.__init__(self)
		self.name = name
		self.counter = counter
		self.delayTime = delayTime

	def run(self):
		print("Ready to running: "+ self.name)
		while (self.counter):
			time.sleep(self.delayTime)
			print("%s: %s"%(self.name, time.ctime(time.time())))
			self.counter -= 1

		print("End a %s"%(self.name))

try:
	threads = []
	thread1 = myThread("thread1", 10, 2)
	thread2 = myThread("thread2", 10, 3)
	thread1.start()
	thread2.start()
	threads.append(thread1)
	threads.append(thread2)
	for i in threads:
		i.join()
	print("End of all threads")
except:
	print("Error when start program!")
