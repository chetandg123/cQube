import time
import unittest

from selenium import webdriver

from Data.Paramters import Data


class Semester_click(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=Data.fpath)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(Data.URL)
        self.driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()
        time.sleep(5)

    def test_semester(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(Data.SR).click()
        time.sleep(5)

    def tearDown(self):
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()