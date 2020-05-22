
import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains

from Data.Paramters import Data
from Testscripts.login_page import Home_page


class blockbtn_click(unittest.TestCase):
    def setUp(self):
        time.sleep(3)

        self.driver = webdriver.Chrome(Data.Path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(Data.URL)

    def test_blockbtn(self):
        print(self.driver.title)
        self.driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(Data.SR).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(Data.Blocks).click()
        time.sleep(10)
        footer = self.driver.find_elements_by_xpath(Data.details)
        for i in range(len(footer)):
            print(footer[i].text)

    # def ClickOn_HomeButton(self):
    #         self.driver.find_element_by_id(Data.Home_icon).click()
    #         print(self.driver.current_url)

    def tearDown(self):
        time.sleep(5)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

