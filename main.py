import os
from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

url = 'https://www.youtube.com/'

print('Открываю браузер')
browser.get(url)
time.sleep(2)
# browser.quit()
# print('Браузер закрыт')

# print('Открываю браузер')
# browser.get(url)
# time.sleep(2)
# browser.quit()
# print('Браузер закрыт')

# print('Открываю браузер')
# browser.get(url)
# time.sleep(2)
# browser.quit()
# print('Браузер закрыт')

# print('Открываю браузер')
# browser.get(url)
# time.sleep(2)
# browser.quit()
# print('Браузер закрыт')

# print('Открываю браузер')
# browser.get(url)
# time.sleep(2)
# browser.quit()
# print('Браузер закрыт')