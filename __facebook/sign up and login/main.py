from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import random 


def verify_account():
	list_email = open("email.txt", 'r').readlines()
	for i in range(len(list_email)):
		list_email[i] = list_email[i][:-2]
		list_email[i] = list_email[i].split('\t')
	return list_email


def firstname_process():
	fs = open("first_name.txt", 'r').readlines()
	return random.choice(fs)


def lastname_process():
	ls = open("last_name.txt", "r").readlines()
	return random.choice(ls)


def email_process():
	em = open("nameemail.txt", "r").readlines()
	return random.choice(em)

def password_process():
	pw = open("password.txt", 'r').readlines()
	return random.choice(pw)



def facebookSignUp(first_name, last_name, email, password, password_email):

	driver = webdriver.Chrome()
	driver.get ("https://facebook.com")
	driver.find_element_by_id("u_0_j").send_keys(first_name) # first name
	driver.find_element_by_id("u_0_l").send_keys(last_name) # last name
	driver.find_element_by_id("u_0_o").send_keys(email) # email
	driver.implicitly_wait(4)
	driver.find_element_by_id("u_0_r").send_keys(email)
	# u_0_r
	driver.find_element_by_id("u_0_v").send_keys(password) # password
	# driver.find_element_by_id("day").send_keys(days) # day
	temp_day = random.choice(range(1, 29))
	temp_month = random.choice(['Tháng 1', 'Tháng 2','Tháng 3', 'Tháng 4','Tháng 5', 'Tháng 6','Tháng 7', 'Tháng 8','Tháng 9', 'Tháng 10', 'Tháng 12'])
	temp_year = random.choice((range(1990, 2000)))
	sex = 'Nam'
	select_days = Select(driver.find_element_by_id('day'))
	select_days.select_by_visible_text(str(temp_day))

	select_month = Select(driver.find_element_by_id('month'))
	select_month.select_by_visible_text(temp_month)

	select_year = Select(driver.find_element_by_id('year'))
	select_year.select_by_visible_text(str(temp_year))

	# driver.find_element_by_id("month").send_keys(months) # month
	# driver.find_element_by_id("year").send_keys(years) #year
	temp = random.choice(range(1,3))
	if temp%2 == 0:
		sex = 'Nam'
		# driver.find_element_by_id("u_0_9").click()
		buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Nam')]")
		for btn in buttons:
			btn.click()

	else :
		sex = 'Nu'
		# driver.find_element_by_id("u_0_a").click()
		buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Nữ')]")
		for btn in buttons:
			btn.click()	

	ac = open("account.txt", 'w')
	ac.write(first_name+ '\t' + last_name + '\t' +  email+ '\t'+ password + '\t'+ str(temp_day) + '\t' + temp_month +'\t'+ str(temp_year) + '\t' + sex)
	driver.find_element_by_id("u_0_11").click() # sign up
	time.sleep(5)
	driver.implicitly_wait(4)
	buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Kết nối với Gmail')]")
	for btn in buttons:
		btn.click()
	driver.implicitly_wait(4)
	driver.find_element_by_name("identifier").send_keys(email)
	driver.find_element_by_id("identifierNext").click()
	driver.implicitly_wait(4)
	driver.find_element_by_name("password").send_keys(password_email)
	driver.find_element_by_id("passwordNext").click()
	# print("Xong tai khoan 1")

	time.sleep(100)

	# id ô nhập code code_in_cliff
	# class con ket noi voi gmail _42ft _4jy0 _4jy4 _4jy1 selected _51sy
	# id email confirm button sau khi login xong an trang ca nhan email_confirmation_button
	# class email trong setting _42ft _42fu SettingsEmailPendingConfirm
	#id code code

a1 = firstname_process()
a2 = lastname_process()
a3 = verify_account()
a4 = password_process()

facebookSignUp(a1, a2, a3[0][0], a4, a3[0][1])