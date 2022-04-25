""" Utils """
from datetime import datetime
import json
import os
import subprocess
from typing import Dict, List
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd

""" Selenium utils """

DEFAULT_WAIT = 5
def get_element(browser, by_method, key, timeout=DEFAULT_WAIT):
	return WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((by_method, key)))

def get_elements(browser, by_method, key):
	return WebDriverWait(browser, DEFAULT_WAIT).until(EC.presence_of_all_elements_located((by_method, key)))

def click_element(browser, by_method, key, timeout=DEFAULT_WAIT):
	element = get_element(browser, by_method, key, timeout=timeout)
	element.click()

def get_element_among(browser, key, id):
	get_elements(browser, By.CLASS_NAME, key)
	# WebDriverWait(browser, DEFAULT_WAIT).until(EC.presence_of_element_located((By.CLASS_NAME, key)))
	element = browser.find_elements_by_class_name(key)[id]
	return element

def click_element_among(browser, key, id):
	# WebDriverWait(browser, DEFAULT_WAIT).until(EC.presence_of_element_located((By.CLASS_NAME, key)))
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

def get_next_to(data: List[str], key: str, offset=1) -> str or None:
	"""
	Return the element next to the found key in a list.
	Return None if the key isn't found, or at the end of the list.
	"""
	for i in range(len(data) - offset):
		if data[i] == key:
			return data[i+offset]
	return None