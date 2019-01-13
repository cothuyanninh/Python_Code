from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import sqlite3

driver = webdriver.Chrome()

def read_db():
	acc = []
	conn = sqlite3.connect('pythonsqlite.db')
	c = conn.cursor()
	for row in c.execute('SELECT DISTINCT * FROM users'):
		acc.append(row)
	return acc

def google_login(username_, password_):

	driver.get ("https://accounts.google.com/ServiceLogin")
	driver.find_element_by_name("identifier").send_keys(username_)
	driver.find_element_by_id("identifierNext").click()
	driver.implicitly_wait(4)
	try:
		driver.find_element_by_name("password").send_keys(password_)
	except:
		driver.quit()
		return
	driver.find_element_by_id("passwordNext").click()
	driver.implicitly_wait(4)
	time.sleep(5)
	# driver.quit()
	driver.get("https://www.textnow.com/signup")
	driver.implicitly_wait(4)
	a = driver.find_element_by_id("google-signup").click()
	


ac = read_db()
for i in range(len(ac)):
	tuple_i = ac[i]
	google_login(tuple_i[1], tuple_i[2])






