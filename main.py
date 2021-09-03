import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from env import USERNAME, PASSWORD, CHROME_DRIVER_PATH
import pandas as pd

""" Contants """
LINK_TO_COURSE = 'slds-truncate.outputLookupLink'

""" Utils """
def get_element(by_method, key, timeout=10):
	return WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((by_method, key)))

def get_elements(by_method, key):
	return WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((by_method, key)))

def click_element(by_method, key):
	element = get_element(by_method, key)
	element.click()

def get_element_among(key, id):
	get_elements(By.CLASS_NAME, key)
	# WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, key)))
	element = browser.find_elements_by_class_name(key)[id]
	return element

def click_element_among(key, id):
	# print('start waiting 10 seconds')
	# print('done waiting')
	# print('list of among:', browser.find_elements_by_class_name(key))
	# WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, key)))
	# element = browser.find_elements_by_class_name(key)[id]
	get_element_among(key, id).click()


""" Helpers """
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
	# click_element(By.CLASS_NAME, 'triggerLinkTextAndIconWrapper.slds-p-right--x-large')
	# click_element_among('forceVirtualAutocompleteMenuOption', 2)
	# sleep(1.5)

def scroll():
	"""Scroll the course list to make more course visible"""
	get_element(By.CLASS_NAME, 'uiScroller.scroller-wrapper.scroll-bidirectional.native')
	SCROLLING_SCRIPT = 'document.getElementsByClassName("uiScroller scroller-wrapper scroll-bidirectional native")[0].scrollTo(0, 10000)'
	browser.execute_script(SCROLLING_SCRIPT)
	sleep(1)

def num_courses():
	return len(browser.find_elements_by_class_name(LINK_TO_COURSE)) // 2

def show_all(count=None):
	sleep(1)
	if count is None:
		scroll()
		scroll()
		scroll()
	else:
		while num_courses() < count:
			scroll()
			print('scrolling')


def get_course_schedule():
	# Wait to load
	get_element(By.CLASS_NAME, LINK_TO_COURSE)

	show_all()
	
	# Get num courses
	count_courses = num_courses()
	# count_courses = 1
	print(f"{count_courses} courses found. Gonna get their schedules ...")

	# Iterate through courses
	data = {}

	for i in range(0, count_courses):
		# Go to one course
		print('Getting coures number', i)
		
		# wait to load
		get_elements(By.CLASS_NAME, LINK_TO_COURSE) 
		sleep(1)
		show_all(i + 1)
		click_element_among(LINK_TO_COURSE, i * 2)
		sleep(1)

		# Get the schedule
		# click_element(By.CLASS_NAME, 'slds-truncate.slds-m-right--xx-small')

		# Get time
		# get_element(By.CLASS_NAME, 'toggle.slds-th__action.slds-text-link--reset ')

		title = get_element(By.CLASS_NAME, 'slds-page-header__title').text
		print(title)

		course = {}

		# METADATA = 'slds-form-element__control.slds-grid.itemBody'
		METADATA = 'slds-grid.slds-gutters_small'
		
		metadata = get_element_among(METADATA, 0).text.split('\n')
		course['title'] = metadata[1]
		term = metadata[3]

		metadata = get_element_among(METADATA, 1).text.split('\n')
		course['id'] = metadata[1]
		course['credits'] = metadata[3]
		
		metadata = get_element_among(METADATA, 2).text.split('\n')
		course['instructor'] = metadata[2]
		
		status = metadata[-1]
		print(status)
		if status == 'Cancelled':
			print("CANCELLED COURSE!!!")
			browser.back()
			continue
		

		# DESCRIPTION = 'test-id__section-content.slds-section__content.section__content'
		
		DESCRIPTION = 'slds-rich-text-editor__output.uiOutputRichText.forceOutputRichText'
		course['description'] = get_element_among(DESCRIPTION, 0).text
		# print(des)
		
		data.setdefault(term, [])
		data[term].append(course)

		course['schedule'] = []
		browser.execute_script('window.scrollTo(0, 10000)')
		SCHEDULE = 'forceRecordLayout.slds-table.slds-no-row-hover.slds-table_cell-buffer.slds-table_fixed-layout.uiVirtualDataGrid--default.uiVirtualDataGrid'

		if 'Fall' in term:
			try:
				schedule_text = get_element(By.CLASS_NAME, SCHEDULE).text
				print(schedule_text.split('\n'))
				blocks = schedule_text.split('\n')
				for block in blocks:
					if not (':' in block):
						continue
					tokens = block.split()
					for day in tokens[2:]:
						course['schedule'].append({
							'day': day.strip(','),
							'start_time': tokens[0],
							'end_time': tokens[1]
						})
				print('Got the schedule :>')
			except:
				print("No schedule")


		# print(des)
		# print(browser.page_source)
		# sleep(10)
		
		# course_id = get_element_among('uiOutputText', 1).text
		# print(f"({i}) Course: {course_id}")
		# data['course'].append(course_id)

		# try:
		# 	schedule = browser.find_elements_by_class_name('cellContainer')
		# 	data['location'].append(schedule[1].text)
		# 	data['start_time'].append(schedule[2].text)
		# 	data['end_time'].append(schedule[3].text)
		# 	data['day'].append(schedule[4].text)
		# except:
		# 	data['location'].append('')
		# 	data['start_time'].append('')
		# 	data['end_time'].append('')
		# 	data['day'].append('')

		
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
	
	for key, value in data.items():
		json.dump(value, open(key + '.json', 'w+'))
	print('Program done. Now check you data file. Thank you!')


