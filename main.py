from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from env import USERNAME, PASSWORD, CHROME_DRIVER_PATH
import pandas as pd

def get_element(by_method, key):
	return WebDriverWait(browser, 10).until(EC.visibility_of_element_located((by_method, key)))

def click_element(by_method, key):
	element = get_element(by_method, key)
	element.click()

def click_element_among(key, id):
	WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, key)))
	element = browser.find_elements_by_class_name(key)[id]
	element.click()

def get_element_among(key, id):
	WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, key)))
	element = browser.find_elements_by_class_name(key)[id]
	return element


def login():
	print('Logging into OneStop ...')
	browser.get('https://onestop.fulbright.edu.vn/')

	# 'Fulbright O365 Login'
	click_element(By.CLASS_NAME, "slds-button")

	username_field = get_element(By.ID, 'i0116')
	username_field.send_keys(USERNAME, Keys.RETURN)

	password_field = get_element(By.ID, 'i0118')
	password_field.send_keys(PASSWORD)

	# 'Sign in' button
	click_element(By.ID, 'idSIButton9')

	# 'Yes' (stayed sign in)
	click_element(By.ID, 'idSIButton9')
	print('Successfully logged in')

def access_enrollment():
	print('Going to "My Enrollment" ...')
	# Go to 'My enrollment'
	click_element_among('main-box', 2)

	# Go to Spring Semester
	click_element(By.CLASS_NAME, 'triggerLinkTextAndIconWrapper.slds-p-right--x-large')
	click_element_among('forceVirtualAutocompleteMenuOption', 2)
	sleep(1.5)

def get_course_schedule():
	get_element(By.CLASS_NAME, 'slds-truncate.outputLookupLink')
	sleep(1)
	count_courses = len(browser.find_elements_by_class_name('slds-truncate.outputLookupLink'))
	print(f"{count_courses} courses found. Gonna get their schedules ...")

	# Iterate through courses
	data = {
		'course': [],
		'location': [],
		'start_time': [],
		'end_time': [],
		'day': [],
	}

	for i in range(count_courses):
		sleep(1)
		get_element(By.CLASS_NAME, 'slds-truncate.outputLookupLink.slds-truncate.forceOutputLookup')
		click_element_among('slds-truncate.outputLookupLink.slds-truncate.forceOutputLookup', i)
		sleep(1)

		# Get the schedule
		click_element(By.CLASS_NAME, 'slds-truncate.slds-m-right--xx-small')

		# Get time
		get_element(By.CLASS_NAME, 'toggle.slds-th__action.slds-text-link--reset ')
		
		course_id = get_element_among('uiOutputText', 1).text
		print(f"({i}) Course: {course_id}")
		data['course'].append(course_id)

		try:
			schedule = browser.find_elements_by_class_name('cellContainer')
			data['location'].append(schedule[1].text)
			data['start_time'].append(schedule[2].text)
			data['end_time'].append(schedule[3].text)
			data['day'].append(schedule[4].text)
		except:
			data['location'].append('')
			data['start_time'].append('')
			data['end_time'].append('')
			data['day'].append('')

		browser.back()
		browser.back()

	return data

def save_data(data):
	print('Save data to "data.csv" file')
	print('data =', data)
	df = pd.DataFrame(data)
	print(df)
	df.to_csv('data.csv')

if __name__ == "__main__":
	browser = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

	login()
	access_enrollment()
	data = get_course_schedule()
	browser.close()
	
	save_data(data)
	print('Program done. Now check you data.csv file. Thank you!')


