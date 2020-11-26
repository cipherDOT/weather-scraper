from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

import time
from dotenv import load_dotenv
import os

load_dotenv()

chromedriver = os.getenv('chromedriver')

chrome_options = Options()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(
    chromedriver,
    chrome_options=chrome_options
)

# place to search is an user input
place = input('Please enter the place of interest: ')

# url for getting the temperature information from Google
url = f'https://www.google.com/search?q=weather at {place}'

# browser to get the url(without opening a browser due to '--headless' argument)
browser.get(url)

# giving time for the browser to load the page
time.sleep(2)

# Handling the NoSuchElement error
try:
    temp = browser.find_element_by_xpath('//*[@id="wob_tm"]')
except NoSuchElementException as e:
    print(e)

# Temperature output
print(f'The temperature in {place.capitalize()} now is {temp.text}°C')
