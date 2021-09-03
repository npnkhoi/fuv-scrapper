from time import sleep
from selenium import webdriver
from env import CHROME_DRIVER_PATH

browser = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
SITE = 'https://www.vox.com/'
browser.get(SITE)
print('scrolling')
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(10)