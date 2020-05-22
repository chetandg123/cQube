import csv
import time
import unittest

from Data.Paramters import Data
from selenium import webdriver

class Home_icon(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(Data.Path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(Data.URL)

    def test_clusterbtn(self):
        print(self.driver.title)
        self.driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(Data.SR).click()

        time.sleep(5)
        print(self.driver.current_url)
        self.driver.find_element_by_xpath(Data.Home_icon).click()
        print(self.driver.current_url)
    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

