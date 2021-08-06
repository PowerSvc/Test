import os
from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--disable-dev-shm-usage")

url = "https://www.youtube.com/"

browser = webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"))
print('Открываю браузер')
browser.get(url)
time.sleep(2)
browser.close()
print('Браузер закрыт')

print('Открываю браузер')
browser.get(url)
time.sleep(2)
browser.close()
print('Браузер закрыт')

print('Открываю браузер')
browser.get(url)
time.sleep(2)
browser.close()
print('Браузер закрыт')

print('Открываю браузер')
browser.get(url)
time.sleep(2)
browser.close()
print('Браузер закрыт')

print('Открываю браузер')
browser.get(url)
time.sleep(2)
browser.close()
print('Браузер закрыт')