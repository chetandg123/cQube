
import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains

from Data.Paramters import Data
from Testscripts.login_page import Home_page


class blockbtn_click(unittest.TestCase):
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
        self.driver.find_element_by_xpath(Data.Clusters).click()
        time.sleep(30)
        count  = self.driver.find_elements_by_xpath(Data.dots)
        self.assertEqual(count,25000,"dots are not found")
        footer = self.driver.find_elements_by_xpath(Data.details)
        for i in range(len(footer)):
            print(footer[i].text)



    def tearDown(self):
        time.sleep(5)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

