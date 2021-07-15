from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC   
import time
import os

acc_user = os.environ.get('username_acc')
acc_pass = os.environ.get('password_acc')


driver = webdriver.Firefox()

driver.get('https://acconline.austincc.edu/')


search = driver.find_element_by_id("okta-signin-username")
search.send_keys(acc_user)
search = driver.find_element_by_id("okta-signin-password")
search.send_keys(acc_pass)
search = driver.find_element_by_id("okta-signin-submit")
search.send_keys(Keys.RETURN)
time.sleep(10)
driver.maximize_window()
complete = False

while not complete:
	try:
		element = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.CSS_SELECTOR, ".eesy_hintfixed_buttons"))
			)
		element.click()

		element = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/div[2]/ul/li[1]/a"))
			)
		element.click()

		element = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.XPATH, "//li[@id='paletteItem:_2736871_1']/a/span"))
			)
		element.click()

		complete = True   

	except:
		print("Tried selecting but failed")
		driver.quit()



