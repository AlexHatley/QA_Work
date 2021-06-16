# Simple Flickr Search Test

from threading import Thread
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import My_BrowserStack_key
import Test_Flickr_Search_Text as search
import unittest

# This array 'caps' defines the capabilities browser, device and OS combinations where the test will run
caps=[{
      'os_version': '10',
      'os': 'Windows',
      'browser': 'chrome',
      'browser_version': '78.0',
      'resolution': '1920x1080',
      'name': 'Parallel Test1', # test name
      'build': 'browserstack-build-1' # Your tests will be organized within this build

      },
      {
      'os_version': 'Big Sur',
      'os': 'OS X',
      'browser': 'Firefox',
      'browser_version': 'latest',
      'resolution': '1920x1080',
      'name': 'Parallel Test2',
      'build': 'browserstack-build-1'
      },
      {
      'os_version': 'Big Sur',
      'os': 'OS X',
      'browser': 'Edge',
      'browser_version': '87.0',
      'resolution': '1920x1080',
      'name': 'Parallel Test3',
      'build': 'browserstack-build-1'
      },
      {
       'os_version': 'Big Sur',
       'os': 'OS X',
       'browser': 'Safari',
       'browser_version': '14.0',
       'resolution': '1920x1080',
       'name': 'Parallel Test4',
       'build': 'browserstack-build-1'
}]
def run_session(desired_cap):
    driver = webdriver.Remote(command_executor=My_BrowserStack_key.key, desired_capabilities=desired_cap)
    driver.get("https://www.flickr.com")
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
    print (N2,"photos are displayed")

    driver.quit()

#The Thread function takes run_session function and each set of capability from the caps array as an argument to run each session parallelly
for cap in caps:
  Thread(target=run_session, args=(cap,)).start()



