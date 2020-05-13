import time
import unittest

from selenium import webdriver

from Data.Paramters import Data


class Xaxis(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(Data.Path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(Data.URL)
        self.driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()
        time.sleep(2)

    def test_click_xaxis(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        head =self.driver.find_element_by_xpath("//td[contains(text(),'CRC Reports ')]").text
        self.driver.find_element_by_xpath(Data.crc).click()
        time.sleep(30)
        xaxis_lists =self.driver.find_elements_by_xpath(Data.xaxis)
        for i in range(len(xaxis_lists)):
            xaxis_lists[i].click()
            time.sleep(10)



    def tearDown(self):
            time.sleep(5)
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()