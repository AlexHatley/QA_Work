# The Simple Test of the part "The Flickr Developer Guide" https://www.flickr.com/services/developer/
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_Chrome_Alex(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_flickr_chrome_max(self):
        driver = self.driver
        driver.set_window_size(1200, 600)  # This is an option
        driver.get("https://www.flickr.com/services/developer/")
        time.sleep(1)
        # It's 'The Flickr Developer Guide'?
        if not "The Flickr Developer Guide" in driver.title:
            raise Exception("Title for 'The Flickr Developer Guide' is wrong!")
        # Page "Home"
        # -------------------------------------------------------------------------------------------------------------
        # Go to 'Community Guidelines/Community'
        driver.find_element(By.LINK_TEXT, "Community Guidelines").click()
        time.sleep(1)
        # It's 'Policies & Guidelines'?
        if not driver.find_element(By.XPATH, "//h1[@class='header-title'][contains(.,'Policies & Guidelines')]"):
            raise Exception("Title for 'Policies & Guidelines' is wrong!")

        # Cookies? - accept!
        driver.implicitly_wait(10)
        # driver.find_element(By.XPATH, "//button[@id='truste-consent-button']").click()
        driver.find_element(By.XPATH, "//*[@class='icon icon-close']").click()
        time.sleep(1)

        # Choice 'Community Guidelines/Terms'
        driver.find_element(By.XPATH, "//span[contains(.,'Terms')]").click()
        time.sleep(1)
        driver.back()
        # Choice' Community Guidelines/Privacy'
        driver.find_element(By.XPATH, "//span[contains(.,'Privacy')]").click()
        time.sleep(1)
        driver.back()
        # Choice 'Community Guidelines/API'
        driver.find_element(By.XPATH, "//span[contains(.,'API')]").click()
        time.sleep(1)
        driver.back()
        # Choice 'Community Guidelines/Community'
        driver.find_element(By.XPATH, "// span[contains(., 'Community')]").click()
        time.sleep(1)
        driver.back()
        # Choice 'Community Guidelines/Cookies'
        driver.find_element(By.XPATH, "//span[contains(.,'Cookies')]").click()
        time.sleep(1)
        driver.back()
        # Choice 'Community Guidelines/Data Processing'
        driver.find_element(By.XPATH, "//span[contains(.,'Data Processing')]").click()
        time.sleep(1)
        driver.back()
        driver.back()
        # -----------------------------------------------------------------------------------------------------------
        # Go to 'Changelog'
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "Changelog").click()
        time.sleep(1)
        # It's 'The Flickr API Changelog'?
        if not driver.find_element(By.XPATH, "//div[contains(.,'The Flickr API Changelog')]"):
            raise Exception("The Flickr API Changelog' is wrong!")
        driver.back()
        # -----------------------------------------------------------------------------------------------------------
        # Go to 'code.flickr.com'
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "code.flickr.com").click()
        time.sleep(1)
        # It's 'code.flickr.com'?
        if not driver.find_element(By.XPATH, "//img[contains(@height,'157')]"):
            raise Exception("The Flickr API Changelog' is wrong!")
        # Choice 'code.flickr.com/Flickr'
        driver.find_element(By.XPATH, "(//a[contains(.,'Flickr')])[1]").click()
        time.sleep(1)
        driver.back()
        # Choice 'code.flickr.com/Flickr Blog'
        driver.find_element(By.XPATH, "//a[contains(.,'Flickr Blog')]").click()
        time.sleep(3)
        driver.back()
        # Choice 'code.flickr.com/@flickr'
        driver.find_element(By.XPATH, "(//a[contains(.,'@flickr')])[1]").click()
        time.sleep(3)
        driver.back()
        # Choice 'code.flickr.com/@flickrapi'
        driver.find_element(By.XPATH, "//a[contains(.,'@flickrapi')]").click()
        time.sleep(3)
        driver.back()
        # Choice 'code.flickr.com/Developer Guidelines'
        driver.find_element(By.XPATH, "//a[contains(.,'Developer Guidelines')]").click()
        time.sleep(2)
        driver.back()
        # Choice 'code.flickr.com/API'
        driver.find_element(By.XPATH, "(//a[contains(.,'API')])[1]").click()
        time.sleep(2)
        driver.back()
        # Choice 'code.flickr.com/Jobs'
        driver.find_element(By.XPATH, "//a[contains(.,'Jobs')]").click()
        time.sleep(3)
        driver.back()
        driver.back()
        # -----------------------------------------------------------------------------------------------------------
        # Go to 'FAQs'
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "FAQs").click()
        time.sleep(1)
        # It's 'FAQs'?
        if not driver.find_element(By.XPATH, "//span[contains(.,'Help Center')]"):
            raise Exception("Help Center' is wrong!")
        driver.back()
        # -----------------------------------------------------------------------------------------------------------
        # Go to 'Flickr API'
        driver.find_element(By.LINK_TEXT, "Flickr API").click()
        time.sleep(1)
        driver.back()
        # =============================================================================================================

        driver.find_element(By.XPATH, "//a[contains(.,'Next: API')]").click()
        time.sleep(5)
        # It's 'The Flickr Developer Guide: API'?
        if not driver.find_element(By.XPATH, "//div[contains(.,'The Flickr Developer Guide: API')]"):
            raise Exception("Title for 'The Flickr Developer Guide: API' is wrong!")
        # Page "API"
        # Go to 'Request an API key'
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, 'Request an API key').click()
        time.sleep(1)
        driver.back()
        # Go to 'the Flickr App Garden'
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "the Flickr App Garden").click()
        time.sleep(1)
        driver.back()
        # Go to 'Flickr's auth flow'
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "Flickr's auth flow").click()
        time.sleep(1)
        driver.back()
        # Go to 'App Garden'
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "App Garden").click()
        time.sleep(1)
        driver.back()
        # =============================================================================================================

        driver.find_element(By.XPATH, "//a[contains(.,'Next: Community')]").click()
        time.sleep(5)
        # It's 'The Flickr Developer Guide: Community'?
        if not driver.find_element(By.XPATH, "// div[contains(., 'The Flickr Developer Guide: Community')]"):
            raise Exception("Title for 'The Flickr Developer Guide: Community' is wrong!")
        # Page "Community"
        # Go to 'Creative Commons licenses'
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "Creative Commons licenses").click()
        time.sleep(1)
        driver.back()
        # =============================================================================================================

        driver.find_element(By.XPATH, "//a[contains(.,'Next: Business')]").click()
        time.sleep(3)
        # It's 'The Flickr Developer Guide: Business'?
        if not driver.find_element(By.XPATH, "// div[contains(., 'The Flickr Developer Guide: Business')]"):
            raise Exception("Title for 'The Flickr Developer Guide: Business' is wrong!")
        # Page "Business "
        # =============================================================================================================

        driver.find_element(By.XPATH, "//a[contains(.,'Next: Attributions')]").click()
        time.sleep(3)
        # It's 'The Flickr Developer Guide: Attributions'?
        if not driver.find_element(By.XPATH, "// div[contains(., 'The Flickr Developer Guide: Attributions')]"):
            raise Exception("Title for 'The Flickr Developer Guide: Attributions' is wrong!")
        # Page "Attributions"
        # =============================================================================================================

        driver.find_element(By.XPATH, "//a[contains(.,'Home')]").click()  # Back to page "Home"
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()  # Close the browser.

class Test_Firefox_Alex(unittest.TestCase):  # Firefox
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_flickr_Firefox_max(self):
        driver = self.driver
        driver.set_window_size(1200, 600)  # This is an option
        driver.get("https://www.flickr.com/services/developer/")
        time.sleep(3)
        # It's 'The Flickr Developer Guide'?
        if not "The Flickr Developer Guide" in driver.title:
            raise Exception("Title for Homepage is wrong!")
        time.sleep(2)
        # Page "Home"
        # -------------------------------------------------------------------------------------------------------------
        # Go to 'Community Guidelines/Community'
        driver.find_element(By.LINK_TEXT, "Community Guidelines").click()
        time.sleep(1)
        # It's 'Policies & Guidelines'?
        if not driver.find_element(By.XPATH, "//h1[@class='header-title'][contains(.,'Policies & Guidelines')]"):
            raise Exception("Title for 'Policies & Guidelines' is wrong!")

        # Cookies? - accept!
        driver.implicitly_wait(10)
#        driver.find_element(By.XPATH, "//button[@id='truste-consent-button']").click()
        driver.find_element(By.XPATH, "//*[@class='icon icon-close']").click()

        time.sleep(1)        # Choice 'Community Guidelines/Terms'
        driver.find_element(By.XPATH, "//span[contains(.,'Terms')]").click()
        time.sleep(1)
        driver.back()
        # Choice' Community Guidelines/Privacy'
        driver.find_element(By.XPATH, "//span[contains(.,'Privacy')]").click()
        time.sleep(1)
        driver.back()
        # Choice 'Community Guidelines/API'
        driver.find_element(By.XPATH, "//span[contains(.,'API')]").click()
        time.sleep(1)
        driver.back()
        # Choice 'Community Guidelines/Community'
        driver.find_element(By.XPATH, "// span[contains(., 'Community')]").click()
        time.sleep(1)
        driver.back()
        # Choice 'Community Guidelines/Cookies'
        driver.find_element(By.XPATH, "//span[contains(.,'Cookies')]").click()
        time.sleep(1)
        driver.back()
        # Choice 'Community Guidelines/Data Processing'
        driver.find_element(By.XPATH, "//span[contains(.,'Data Processing')]").click()
        time.sleep(1)
        driver.back()
        driver.back()
        # -----------------------------------------------------------------------------------------------------------
        # Go to 'Changelog'
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "Changelog").click()
        time.sleep(1)
        # It's 'The Flickr API Changelog'?
        if not driver.find_element(By.XPATH, "//div[contains(.,'The Flickr API Changelog')]"):
            raise Exception("The Flickr API Changelog' is wrong!")
        driver.back()
        # -----------------------------------------------------------------------------------------------------------
        # Go to 'code.flickr.com'
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "code.flickr.com").click()
        time.sleep(1)
        # It's 'code.flickr.com'?
        if not driver.find_element(By.XPATH, "//img[contains(@height,'157')]"):
            raise Exception("The Flickr API Changelog' is wrong!")
        # Choice 'code.flickr.com/Flickr'
        driver.find_element(By.XPATH, "(//a[contains(.,'Flickr')])[1]").click()
        time.sleep(1)
        driver.back()
        # Choice 'code.flickr.com/Flickr Blog'
        driver.find_element(By.XPATH, "//a[contains(.,'Flickr Blog')]").click()
        time.sleep(3)
        driver.back()
        # Choice 'code.flickr.com/@flickr'
        driver.find_element(By.XPATH, "(//a[contains(.,'@flickr')])[1]").click()
        time.sleep(3)
        driver.back()
        # Choice 'code.flickr.com/@flickrapi'
        driver.find_element(By.XPATH, "//a[contains(.,'@flickrapi')]").click()
        time.sleep(3)
        driver.back()
        # Choice 'code.flickr.com/Developer Guidelines'
        driver.find_element(By.XPATH, "//a[contains(.,'Developer Guidelines')]").click()
        time.sleep(2)
        driver.back()
        # Choice 'code.flickr.com/API'
        driver.find_element(By.XPATH, "(//a[contains(.,'API')])[1]").click()
        time.sleep(2)
        driver.back()
        # Choice 'code.flickr.com/Jobs'
        driver.find_element(By.XPATH, "//a[contains(.,'Jobs')]").click()
        time.sleep(3)
        driver.back()
        driver.back()
        # -----------------------------------------------------------------------------------------------------------
        # Go to 'FAQs'
        time.sleep(10)
        driver.find_element(By.LINK_TEXT, "FAQs").click()
        time.sleep(5)
        # It's 'FAQs'?
        if not driver.find_element(By.XPATH, "//span[contains(.,'Help Center')]"):
            raise Exception("Help Center' is wrong!")
        driver.back()
        # -----------------------------------------------------------------------------------------------------------
        # Go to 'Flickr API'
        driver.find_element(By.LINK_TEXT, "Flickr API").click()
        time.sleep(1)
        driver.back()
        # =============================================================================================================

        driver.find_element(By.XPATH, "//a[contains(.,'Next: API')]").click()
        time.sleep(5)
        # It's 'The Flickr Developer Guide: API'?
        if not driver.find_element(By.XPATH, "//div[contains(.,'The Flickr Developer Guide: API')]"):
            raise Exception("Title for 'The Flickr Developer Guide: API' is wrong!")
        # Page "API"
        # Go to 'Request an API key'
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, 'Request an API key').click()
        time.sleep(1)
        driver.back()
        # Go to 'the Flickr App Garden'
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "the Flickr App Garden").click()
        time.sleep(1)
        driver.back()
        # Go to 'Flickr's auth flow'
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "Flickr's auth flow").click()
        time.sleep(1)
        driver.back()
        # Go to 'App Garden'
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "App Garden").click()
        time.sleep(1)
        driver.back()
        # =============================================================================================================

        driver.find_element(By.XPATH, "//a[contains(.,'Next: Community')]").click()
        time.sleep(5)
        # It's 'The Flickr Developer Guide: API'?
        if not driver.find_element(By.XPATH, "// div[contains(., 'The Flickr Developer Guide: Community')]"):
            raise Exception("Title for 'The Flickr Developer Guide: Community' is wrong!")
        # Page " Community"
        # Go to 'Creative Commons licenses'
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "Creative Commons licenses").click()
        time.sleep(1)
        driver.back()
        # =============================================================================================================

        driver.find_element(By.XPATH, "//a[contains(.,'Next: Business')]").click()
        time.sleep(5)
        # It's 'The Flickr Developer Guide: Business'?
        if not driver.find_element(By.XPATH, "// div[contains(., 'The Flickr Developer Guide: Business')]"):
            raise Exception("Title for 'The Flickr Developer Guide: Business' is wrong!")
        # Page "Business "
        # =============================================================================================================

        driver.find_element(By.XPATH, "//a[contains(.,'Next: Attributions')]").click()
        time.sleep(5)
        # It's 'The Flickr Developer Guide: Attributions'?
        if not driver.find_element(By.XPATH, "// div[contains(., 'The Flickr Developer Guide: Attributions')]"):
            raise Exception("Title for 'The Flickr Developer Guide: Attributions' is wrong!")
        # Page "Attributions"
        # =============================================================================================================

        driver.find_element(By.XPATH, "//a[contains(.,'Home')]").click()  # Back to page "Home"
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()  # Close the browser
        time.sleep(1)
class Test_Edge_Alex(unittest.TestCase):  # Edge
    def setUp(self):

        self.driver = webdriver.Edge('msedgedriver.exe')   # Edge's filename is important!!!
#        self.driver = webdriver.Edge(executable_path='C:\WebDriver\msedgedriver.exe')  # It's OK too!
#        self.driver = webdriver.Edge(r'C:\WebDriver\msedgedriver.exe')  # It's OK too!
        time.sleep(10)
        self.driver.maximize_window()
    def test_flickr_Edge_max(self):
        driver = self.driver
        driver.set_window_size(1200, 600)  # This is an option
        time.sleep(1)
        driver.get("https://www.flickr.com/services/developer/")
        time.sleep(3)
        # # It's 'The Flickr Developer Guide'?
        if not "The Flickr Developer Guide" in driver.title:
            raise Exception("Title for Homepage is wrong!")
        time.sleep(2)
        # Page "Home"
        # -------------------------------------------------------------------------------------------------------------
        # Go to 'Community Guidelines/Community'
        driver.find_element(By.LINK_TEXT, "Community Guidelines").click()
        time.sleep(1)
        # It's 'Policies & Guidelines'?
        if not driver.find_element(By.XPATH, "//h1[@class='header-title'][contains(.,'Policies & Guidelines')]"):
            raise Exception("Title for 'Policies & Guidelines' is wrong!")

        # Cookies? - accept!
        driver.implicitly_wait(10)
        #        driver.find_element(By.XPATH, "//button[@id='truste-consent-button']").click()
        driver.find_element(By.XPATH, "//*[@class='icon icon-close']").click()
        time.sleep(1)

        # Choice 'Community Guidelines/Terms'
        driver.find_element(By.XPATH, "//span[contains(.,'Terms')]").click()
        time.sleep(1)
        driver.back()
        # Choice' Community Guidelines/Privacy'
        driver.find_element(By.XPATH, "//span[contains(.,'Privacy')]").click()
        time.sleep(1)
        driver.back()
        # Choice 'Community Guidelines/API'
        driver.find_element(By.XPATH, "//span[contains(.,'API')]").click()
        time.sleep(1)
        driver.back()
        # Choice 'Community Guidelines/Community'
        driver.find_element(By.XPATH, "// span[contains(., 'Community')]").click()
        time.sleep(1)
        driver.back()
        # Choice 'Community Guidelines/Cookies'
        driver.find_element(By.XPATH, "//span[contains(.,'Cookies')]").click()
        time.sleep(1)
        driver.back()
        # Choice 'Community Guidelines/Data Processing'
        driver.find_element(By.XPATH, "//span[contains(.,'Data Processing')]").click()
        time.sleep(1)
        driver.back()
        driver.back()
        # -----------------------------------------------------------------------------------------------------------
        # Go to 'Changelog'
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "Changelog").click()
        time.sleep(1)
        # It's 'The Flickr API Changelog'?
        if not driver.find_element(By.XPATH, "//div[contains(.,'The Flickr API Changelog')]"):
            raise Exception("The Flickr API Changelog' is wrong!")
        driver.back()
        # -----------------------------------------------------------------------------------------------------------
        # Go to 'code.flickr.com'
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "code.flickr.com").click()
        time.sleep(1)
        # It's 'code.flickr.com'?
        if not driver.find_element(By.XPATH, "//img[contains(@height,'157')]"):
            raise Exception("The Flickr API Changelog' is wrong!")
        # Choice 'code.flickr.com/Flickr'
        driver.find_element(By.XPATH, "(//a[contains(.,'Flickr')])[1]").click()
        time.sleep(1)
        driver.back()
        # Choice 'code.flickr.com/Flickr Blog'
        driver.find_element(By.XPATH, "//a[contains(.,'Flickr Blog')]").click()
        time.sleep(3)
        driver.back()
        # Choice 'code.flickr.com/@flickr'
        driver.find_element(By.XPATH, "(//a[contains(.,'@flickr')])[1]").click()
        time.sleep(3)
        driver.back()
        # Choice 'code.flickr.com/@flickrapi'
        driver.find_element(By.XPATH, "//a[contains(.,'@flickrapi')]").click()
        time.sleep(3)
        driver.back()
        # Choice 'code.flickr.com/Developer Guidelines'
        driver.find_element(By.XPATH, "//a[contains(.,'Developer Guidelines')]").click()
        time.sleep(2)
        driver.back()
        # Choice 'code.flickr.com/API'
        driver.find_element(By.XPATH, "(//a[contains(.,'API')])[1]").click()
        time.sleep(2)
        driver.back()
        # Choice 'code.flickr.com/Jobs'
        driver.find_element(By.XPATH, "//a[contains(.,'Jobs')]").click()
        time.sleep(3)
        driver.back()
        driver.back()
        # -----------------------------------------------------------------------------------------------------------
        # Go to 'FAQs'
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "FAQs").click()
        time.sleep(1)
        # It's 'FAQs'?
        if not driver.find_element(By.XPATH, "//span[contains(.,'Help Center')]"):
            raise Exception("Help Center' is wrong!")
        driver.back()
        # -----------------------------------------------------------------------------------------------------------
        # Go to 'Flickr API'
        driver.find_element(By.LINK_TEXT, "Flickr API").click()
        time.sleep(1)
        driver.back()
        # =============================================================================================================

        driver.find_element(By.XPATH, "//a[contains(.,'Next: API')]").click()
        time.sleep(5)
        # It's 'The Flickr Developer Guide: API'?
        if not driver.find_element(By.XPATH, "//div[contains(.,'The Flickr Developer Guide: API')]"):
            raise Exception("Title for 'The Flickr Developer Guide: API' is wrong!")
        # Page "API"
        # Go to 'Request an API key'
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, 'Request an API key').click()
        time.sleep(1)
        driver.back()
        # Go to 'the Flickr App Garden'
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "the Flickr App Garden").click()
        time.sleep(1)
        driver.back()
        # Go to 'Flickr's auth flow'
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "Flickr's auth flow").click()
        time.sleep(1)
        driver.back()
        # Go to 'App Garden'
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "App Garden").click()
        time.sleep(1)
        driver.back()
        # =============================================================================================================

        driver.find_element(By.XPATH, "//a[contains(.,'Next: Community')]").click()
        time.sleep(5)
        # It's 'The Flickr Developer Guide: API'?
        if not driver.find_element(By.XPATH, "// div[contains(., 'The Flickr Developer Guide: Community')]"):
            raise Exception("Title for 'The Flickr Developer Guide: Community' is wrong!")
        # Page " Community"
        # Go to 'Creative Commons licenses'
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "Creative Commons licenses").click()
        time.sleep(1)
        driver.back()
        # =============================================================================================================

        driver.find_element(By.XPATH, "//a[contains(.,'Next: Business')]").click()
        time.sleep(5)
        # It's 'The Flickr Developer Guide: Business'?
        if not driver.find_element(By.XPATH, "// div[contains(., 'The Flickr Developer Guide: Business')]"):
            raise Exception("Title for 'The Flickr Developer Guide: Business' is wrong!")
        # Page "Business "
        # =============================================================================================================

        driver.find_element(By.XPATH, "//a[contains(.,'Next: Attributions')]").click()
        time.sleep(5)
        # It's 'The Flickr Developer Guide: Attributions'?
        if not driver.find_element(By.XPATH, "// div[contains(., 'The Flickr Developer Guide: Attributions')]"):
            raise Exception("Title for 'The Flickr Developer Guide: Attributions' is wrong!")
        # Page "Attributions"
        # =============================================================================================================

        driver.find_element(By.XPATH, "//a[contains(.,'Home')]").click()  # Back to page "Home"
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()  # Close the browser

if __name__ == '__main__':
    unittest.main()
