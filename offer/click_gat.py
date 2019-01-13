from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
try:
	driver.set_page_load_timeout(10)
	driver.get("http://gatvler.com/")
except Exception:
	driver.implicitly_wait(6)
	print("Processing")
	try:
		driver.find_element_by_id("B2").click()
	except:
		print("Khong load duoc B2")
# driver.implicitly_wait(4)
# buttons_vietnam = driver.find_elements_by_xpath("//*[contains(text(), 'Cho phép')]")
# if (len(buttons_vietnam) != 0):
#     for btn in buttons_vietnam:
#         btn.click()
# buttons_english = driver.find_elements_by_xpath("//*[contains(text(), 'Allow')]")
# if (len(buttons_english) != 0):
#     for btn in buttons_english:
#         btn.click()

driver.quit()