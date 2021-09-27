from src.parser import get_categories, get_schedule
from time import sleep
from src.utils import click_element_among, get_element, get_element_among, get_elements
from selenium.webdriver.common.by import By

LINK_TO_COURSE = 'slds-truncate.outputLookupLink'
DESCRIPTION = 'slds-rich-text-editor__output.uiOutputRichText.forceOutputRichText'
SCHEDULE = 'forceRecordLayout.slds-table.slds-no-row-hover.slds-table_cell-buffer.slds-table_fixed-layout.uiVirtualDataGrid--default.uiVirtualDataGrid'
METADATA = 'slds-grid.slds-gutters_small'
# METADATA = 'slds-form-element__control.slds-grid.itemBody'
# DESCRIPTION = 'test-id__section-content.slds-section__content.section__content'
CURRENT_TERM = 'Fall' # NOTICE: Update this!

def scroll(browser):
	"""Scroll the course list to make more course visible"""
	get_element(browser, By.CLASS_NAME, 'uiScroller.scroller-wrapper.scroll-bidirectional.native')
	SCROLLING_SCRIPT = 'document.getElementsByClassName("uiScroller scroller-wrapper scroll-bidirectional native")[0].scrollTo(0, 10000)'
	browser.execute_script(SCROLLING_SCRIPT)
	sleep(1)

def num_courses(browser):
	return len(browser.find_elements_by_class_name(LINK_TO_COURSE)) // 2

def show_all(browser, count=None):
	sleep(1)
	if count is None:
		scroll(browser)
		scroll(browser)
		scroll(browser)
	else:
		while num_courses(browser) < count:
			scroll(browser)
			print('scrolling')

def get_course_schedule(browser):
	# Wait to load
	get_element(browser, By.CLASS_NAME, LINK_TO_COURSE)
	show_all(browser)
	# count_courses = num_courses(browser)
	count_courses = 1
	print(f"{count_courses} courses found. Gonna get their schedules ...")

	# Iterate through courses
	data = {}
	for i in range(0, count_courses):
		print('Getting coures number', i)
		course = {}
		
		# wait to load
		get_elements(browser, By.CLASS_NAME, LINK_TO_COURSE) 
		sleep(1)
		show_all(browser, i + 1)
		click_element_among(browser, LINK_TO_COURSE, i * 2)
		sleep(1)

    # Get all the easy fields
		course_id = get_element(browser, By.CLASS_NAME, 'slds-page-header__title').text
		print(course_id)
		metadata = get_element_among(browser, METADATA, 0).text.split('\n')
		course['title'] = metadata[1]
		term = metadata[3]
		metadata = get_element_among(browser, METADATA, 1).text.split('\n')
		course['id'] = metadata[1]
		course['credits'] = metadata[3]
		metadata = get_element_among(browser, METADATA, 2).text.split('\n')
		course['instructor'] = metadata[2]
		
    # Get description (if not cancelled)
		status = metadata[-1]
		if status == 'Cancelled':
			print("CANCELLED COURSE!!!")
			browser.back()
			continue
		course['description'] = get_element_among(browser, DESCRIPTION, 0).text
		course['categories'] = get_categories(course['description'])
		
    # Get schedule
		course['schedule'] = []
		browser.execute_script('window.scrollTo(0, 10000)')
		if CURRENT_TERM in term:
			try:
				schedule_text = get_element(browser, By.CLASS_NAME, SCHEDULE).text
				course['schedule'] = get_schedule(schedule_text)
				print('Got the schedule :>')
			except:
				print("No schedule")

    # Save and go back
		data.setdefault(term, [])
		data[term].append(course)
		browser.back()

	return data