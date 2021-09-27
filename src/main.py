from src.get_courses import get_course_schedule
import json
from selenium import webdriver
from env import CHROME_DRIVER_PATH
from src.init import access_enrollment, login

if __name__ == "__main__":
	browser = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
	login(browser)
	access_enrollment(browser)
	data = get_course_schedule(browser)
	browser.close()
	
	for key, value in data.items():
		json.dump(value, open(key + '.json', 'w+'))
	print('Program done. Now check you data file. Thank you!')


