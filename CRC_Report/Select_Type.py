import time
import unittest

from selenium import webdriver

from Data.Paramters import Data


class Sel_type(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(Data.Path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(Data.URL)
        self.driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()
        time.sleep(2)

    def test_select_for_download(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        head =self.driver.find_element_by_xpath("//td[contains(text(),'CRC Reports ')]").text
        self.driver.find_element_by_xpath(Data.crc).click()
        time.sleep(30)
        sel_type =self.driver.find_elements_by_xpath(Data.seltype)
        time.sleep(5)
        for i in range(len(sel_type)):
            print(sel_type[i].text)
            time.sleep(10)


    def tearDown(self):
            time.sleep(5)
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()