from selenium import webdriver
import time


def fb_login(username_, password_):
	driver = webdriver.Chrome()
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
	time.sleep(5)
	driver.quit()

a = open('result.txt', 'r', encoding= 'utf-8').readlines()

for i in range(20, len(a)):
	b = a[i].split('\t')
	fb_login(b[2].split('\n')[0], b[1])