import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

# script to choose district , block ,cluster and mouse over on last
from Data.Paramters import Data


class Zoom(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(Data.Path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(Data.URL)
        print(self.driver.title)
        self.driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()
        time.sleep(5)

    def test_zoom_in(self):
        self.driver.find_element_by_xpath(Data.zoom_in).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(Data.zoom_out).click()


    def test_zoom_out(self):
        self.driver.find_element_by_xpath(Data.zoom_in).click()
        time.sleep(5)

        self.driver.find_element_by_xpath(Data.zoom_out).click()

    def tearDown(self):
            time.sleep(5)
            self.driver.close()

if __name__ == "__main__":
        unittest.main()
