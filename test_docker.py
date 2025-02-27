from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

global driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.docker.com/")
time.sleep(10)

link = driver.find_elements(By.TAG_NAME,'a')
for a in link:
    print(a.get_attribute('href'))
