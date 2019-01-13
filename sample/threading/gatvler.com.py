from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
import os, time, random
import threading

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_drive = os.getcwd() + "\\chromedriver.exe"

class View(threading.Thread):
	def __init__(self, url, chrome_options, chrome_drive):
		threading.Thread.__init__(self)
		self.url = url
		self.chrome_options = chrome_options
		self.chrome_drive = chrome_drive

	def run(self):
		driver = webdriver.Chrome(chrome_options= self.chrome_options, executable_path = self.chrome_drive)
		driver.get(self.url)
		driver.implicitly_wait(10)
		button_play = driver.find_element_by_class_name("td-icon-search")
		button_play.click()
		driver.implicitly_wait(10)
		time.sleep(10)
		driver.get_screenshot_as_file("capture.png")
		driver.close()
url = "http://gatvler.com/dam-tre-nha-bau-duc-don-halloween-day-nhi-nho/" #+ str(random.randint(0,3)) + "s"
threads = []
try:

	thread1 = View(url, chrome_options, chrome_drive)
	# thread2 = View(url, chrome_options, chrome_drive)
	# thread3 = View(url, chrome_options, chrome_drive)
	# thread4 = View(url, chrome_options, chrome_drive)
	thread1.start()
	# thread2.start() 
	# thread3.start()
	# thread4.start()
except:
	print("Error.")

