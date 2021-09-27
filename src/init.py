from env import USERNAME, PASSWORD, CHROME_DRIVER_PATH
from src.utils import click_element, click_element_among, get_element, get_element_among, get_elements
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def login(browser):
	print('Logging into OneStop ...')
	browser.get('https://onestop.fulbright.edu.vn/')

	# 'Fulbright O365 Login'
	click_element(browser, By.CLASS_NAME, "slds-button")

	username_field = get_element(browser, By.ID, 'i0116')
	username_field.send_keys(USERNAME, Keys.RETURN)

	password_field = get_element(browser, By.ID, 'i0118')
	password_field.send_keys(PASSWORD)

	# 'Sign in' button
	click_element(browser, By.ID, 'idSIButton9')

	# 'Yes' (stayed sign in)
	click_element(browser, By.ID, 'idSIButton9')
	print('Successfully logged in')

def access_enrollment(browser):
	print('Going to "My Enrollment" ...')
	# Go to 'My enrollment'
	click_element_among(browser, 'main-box', 2)

	# Go to Spring Semester
	# click_element(browser, By.CLASS_NAME, 'triggerLinkTextAndIconWrapper.slds-p-right--x-large')
	# click_element_among(browser, 'forceVirtualAutocompleteMenuOption', 2)
	# sleep(1.5)