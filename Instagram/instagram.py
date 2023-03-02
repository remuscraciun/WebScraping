from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import wget
import os
import keyword
import os.path
from os import path

# Credentials and search criteria
username =  # ADD YOUR USERNAME
password =  # ADD YOUR PASSWORD
keyword =  # ADD YOUR SEARCH KEYWORD

# Browser settings

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.set_window_size(750, 750)
driver.get("https://www.instagram.com/")

# Validate only essential cookies dialog
only_essential_cookies = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='_a9-- _a9_1']"))).click()

# Gather CSS selectors for username and password fields and add the contents of "username" and "password" variables declared above
username_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
username_input.clear()
password_input.clear()
username_input.send_keys(username)
password_input.send_keys(password)

# Gather CSS selector
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[class='_acan _acap _acas _aj1-']")))
login_button.click()
time.sleep(5)

# Get rid of annoying 'Not now' dialogs
not_now_dialog1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[class='_acan _acao _acas _aj1-']")))
not_now_dialog1.click()
not_now_dialog2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='_a9-- _a9_1']")))
not_now_dialog2.click()

# Search button
search = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class='_aauy']")))
search.send_keys(keyword)
time.sleep(2)
search.send_keys(Keys.ARROW_DOWN)
search.send_keys(Keys.ENTER)
time.sleep(5)

# Scroll to a set of coordinates to load more images
driver.execute_script("window.scrollTo(0, 4000);")

# Find all image tags
images = driver.find_elements(By.TAG_NAME, "img")
images = [image.get_attribute('src') for image in images]

# Create folder where images are getting downloaded
path = os.getcwd()
path = os.path.join(path, keyword[1:])
if os.path.isdir('cats') == False:
    os.mkdir(path)

print(images)

for index, image in enumerate(images):
    if index > 2:
        save_as = os.path.join(path, keyword + str(index) + '.jpg')
        wget.download(image, save_as)
