from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
chrome_driver = os.getcwd() +"\\chromedriver.exe"

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
driver.get("https://www.youtube.com/watch?v=HaG9bXkvWag")
# ahihi = driver.find_element_by_class_name("style-scope ytd-toggle-button-renderer style-text")
# lucky_button = driver.find_element_by_css_selector("[name=btnI]")
# lucky_button.click()
driver.implicitly_wait(10)
# capture the screen
# driver.get_screenshot_as_file("capture.png")
driver.close()