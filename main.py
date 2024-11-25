from selenium import webdriver
from selenium.webdriver.common.service import Service
import time


service = Service( executable_path = "chromedriver.exe")
driver = webdriver.Chrome(service=Service)

driver.get("https://www.google.com/")

time.sleep(10)

driver.quit()