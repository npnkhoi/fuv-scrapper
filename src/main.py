from src.get_courses import get_course_schedule
from selenium import webdriver
from env import FIREFOX_DRIVER_PATH
from src.init import access_enrollment, login
import click
from src.utils import current_time, save_json

@click.command()
@click.argument('term-id', type=int) # 1-based, from Fall2021
def main(term_id):
	tic = current_time()
	browser = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH)
	login(browser)
	access_enrollment(browser, term_id)
	data = get_course_schedule(browser)
	browser.close()
	save_json(data, tic)

if __name__ == "__main__":
	main()
