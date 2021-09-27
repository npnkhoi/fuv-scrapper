""" Utils """
from typing import List
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd

""" Selenium utils """
def get_element(browser, by_method, key, timeout=10):
	return WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((by_method, key)))

def get_elements(browser, by_method, key):
	return WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((by_method, key)))

def click_element(browser, by_method, key):
	element = get_element(browser, by_method, key)
	element.click()

def get_element_among(browser, key, id):
	get_elements(browser, By.CLASS_NAME, key)
	# WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, key)))
	element = browser.find_elements_by_class_name(key)[id]
	return element

def click_element_among(browser, key, id):
	# print('start waiting 10 seconds')
	# print('done waiting')
	# print('list of among:', browser.find_elements_by_class_name(key))
	# WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, key)))
	# element = browser.find_elements_by_class_name(key)[id]
	get_element_among(browser, key, id).click()

""" Others """
def save_data(data):
	print('Save data to "data.csv" file')
	print('data =', data)
	df = pd.DataFrame(data)
	print(df)
	df.to_csv('data.csv')