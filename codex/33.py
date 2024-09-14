from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time

# replace with the path to your chromedriver executable
chromedriver_path='path/to/chromedriver'

# set up the webdriver
driver=webdriver.chrome(chromedriver_path)
driver.get ('https://web.whatsapp.com')

# wait for the user to scan the QR code
time.sleep(10)

# replace with the target phone
target_number='+254796284644'

#find he search box and enter the target number
search-box=driver .find_element_by_xpath('//*[@id="side"]')