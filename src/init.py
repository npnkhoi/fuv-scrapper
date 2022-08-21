from time import sleep
from env import USERNAME, PASSWORD
from src.utils import click_element, click_element_among, get_element, get_element_among, get_elements
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome

TERM_SELECTOR = 'triggerLinkText.selectedListView.slds-page-header__title'
TERM_OPTION = 'virtualAutocompleteOptionText'

def login(browser: Chrome) -> None:
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

	# Start authentication
	current = browser.switch_to.active_element
	current.send_keys(Keys.RETURN)

	# 'Yes' (stayed sign in)
	print('You have 60 seconds for 2FA authentication')
	click_element(browser, By.ID, 'idSIButton9', timeout=60)
	print('Successfully logged in')

def access_enrollment(browser, term_id: int) -> None:
	print('Going to "My Enrollment" ...')
	# Go to 'My enrollment'
	click_element_among(browser, 'main-box', 2)

	# Go to targeted term
	print('Going to targeted term')
	click_element(browser, By.CLASS_NAME, TERM_SELECTOR)
	click_element_among(browser, TERM_OPTION, term_id)
	sleep(1.5)