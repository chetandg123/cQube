import time
import unittest

from selenium import webdriver

from Data.Paramters import Data


class Dash_menu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(Data.Path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(Data.URL)
        self.driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()
        time.sleep(2)

    def test_menu(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        head = self.driver.find_element_by_xpath("//h4").text
        self.assertEqual("cQube - Dashboard",head,"Not matching words in Page")
    def tearDown(self):
            time.sleep(5)
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()