from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Correct import
import time

# Correctly initialize the Service with the path to the ChromeDriver
service = Service(executable_path="chromedriver.exe")

# Pass the service object to the Chrome driver
driver = webdriver.Chrome(service=service)

# Navigate to the desired webpage
driver.get("https://www.google.com/")

# Pause for 10 seconds
time.sleep(10)

# Quit the driver

