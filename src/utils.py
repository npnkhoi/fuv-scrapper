""" Utils """
from datetime import datetime
import json
import os
import subprocess
from typing import Dict
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
	# WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, key)))
	# element = browser.find_elements_by_class_name(key)[id]
	get_element_among(browser, key, id).click()

""" Others """

def current_time():
	return datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

def save_csv(data):
	print('data =', data)
	df = pd.DataFrame(data)
	print(df)
	df.to_csv('data.csv')

def save_json(data: Dict, timestamp: str) -> None:
	subprocess.run(['mkdir', '-p', os.path.join('logs', timestamp)])
	for key, value in data.items():
		json.dump(value, open(os.path.join('logs', timestamp, key + '.json') , 'w+'))
	print('Data saved at', timestamp)
	print('Now is', current_time())