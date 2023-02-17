from src.get_courses import get_course_schedule, CURRENT_TERM
from selenium import webdriver
from env import CHROME_DRIVER_PATH
from src.init import access_enrollment, login
import click
from src.utils import current_time, save_json
from selenium.webdriver.chrome.options import Options

@click.command()
@click.argument('term-id', type=int) # 1-based, from Fall2021
@click.option('--headless', type=bool, default=True) # 1-based, from Fall2021
def main(term_id, headless):
	print(f"Current term is: {CURRENT_TERM} -- Please update if needed.")
	tic = current_time()
	options = Options()
	options.headless = headless
	options.add_argument("window-size=1920,1080")
	browser = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=options)
	print ("Headless Chrome Initialized")
	
	print('Start login ...')
	login(browser)

	size = browser.get_window_size()
	print("Window size: width = {}px, height = {}px".format(size["width"], size["height"]))

	access_enrollment(browser, term_id)
	data = get_course_schedule(browser)
	browser.close()
	save_json(data, tic)

if __name__ == "__main__":
	main()
