import time
import unittest

from selenium import webdriver

from Data import Paramters
from Data.Paramters import Data
from Testscripts.login_page import Home_page

class Blocks(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(Data.Path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(Data.URL)
        print(self.driver.title)
        self.driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()
        time.sleep(10)

    def test_click_on_blocksbtn(self):
        self.driver.find_element_by_xpath(Data.Blocks).click()
        print(self.driver.current_url)


    def tearDown(self):
        time.sleep(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
