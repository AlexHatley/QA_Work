# Simple Flickr Search Test

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import unittest
import Test_Flickr_Search_Text as search 



driver = webdriver.Chrome()
driver.set_window_size(1200, 1000)
driver.get("https://www.flickr.com/")
time.sleep(1)
# Cookies banner? - accept!      
try:
    driver.find_element(By.XPATH, "//*[@class='icon icon-close']").click()
except NoSuchElementException:
    print("Аnother сookies banner!")
try:
    driver.find_element(By.XPATH, "//button[@id='truste-consent-button']").click()
except NoSuchElementException:
    print("Аnother сookies banner!")
# -------------- Flickr Search ----------------
driver.find_element(By.CLASS_NAME, "search-icon-button").click()
search_text=search.text1
time.sleep(1)
driver.find_element(By.CLASS_NAME, "search-box").send_keys(search_text)
driver.find_element(By.CLASS_NAME,"search-icon-button").click()
# ---------------- Check 1 --------------------
time.sleep(5)
print ("Flickr search photos with text:", search_text)
content1 =driver.find_element(By.PARTIAL_LINK_TEXT,"View all").text
# print (content1)
N1=content1[9:]
print (N1, "photos are found")
N1=len(driver.find_elements(By.CLASS_NAME,"overlay"))
print (N1,"photos are displayed\r")
# ---------------- Check 2 --------------------
print ("Click on 'View all'")
driver.find_element(By.PARTIAL_LINK_TEXT,"View all").click()
time.sleep(5)
content2 =driver.find_element(By.XPATH,"//span[@class='secondary']").text
print (content2)
N2=len(driver.find_elements(By.CLASS_NAME,"overlay"))
print (N2,"photos are displayed\r")
print ("THE END")
driver.quit()
