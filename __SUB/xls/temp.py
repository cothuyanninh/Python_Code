from selenium import webdriver
import time


def fb_login(username_, password_):
	driver = webdriver.Chrome()
	driver.get ("https://accounts.google.com/ServiceLogin")
	# driver.find_element_by_id("identifierId").send_keys(username)
	driver.find_element_by_name("identifier").send_keys(username_)
	driver.find_element_by_id("identifierNext").click()
	driver.implicitly_wait(4)
	driver.find_element_by_name("password").send_keys(password_)
	driver.find_element_by_id("passwordNext").click()
	# time.sleep(5)
	driver.get("https://www.youtube.com/channel/UCsg1-IVAUL5grRiwida9QJg")
	driver.implicitly_wait(4)
	# driver.find_element_by_id("background").click()
	

	# driver.quit()

a = open('result.txt', 'r', encoding= 'utf-8').readlines()

fb_login('NguyenVanQuy_t57@hus.edu.vn', '12000755')
# for i in range(212, len(a)):
# 	b = a[i].split('\t')
# 	# print(b[1])
# 	fb_login(b[2].split('\n')[0], b[1])