import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

# script to click on crc reports
from Data.Paramters import Data


class CRC(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(Data.Path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(Data.URL)
        self.driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()
        time.sleep(10)

    def test_crcreports(self):

        self.driver.find_element_by_xpath(Data.Dashboard).click()
        time.sleep(5)

        self.driver.find_element_by_xpath(Data.crc).click()
        print(self.driver.title)


    def tearDown(self):
            time.sleep(5)
            self.driver.close()

if __name__ == "__main__":
        unittest.main()
