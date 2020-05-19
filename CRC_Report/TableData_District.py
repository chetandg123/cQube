import time
import unittest

from selenium import webdriver

from Data.Paramters import Data


class Crc_Reports(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(Data.Path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(Data.URL)
        self.driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()
        time.sleep(5)

    def test_crcclick(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Data.crc).click()
        time.sleep(30)
        headers = self.driver.find_elements_by_xpath(Data.headers)
        for i in range(len(headers)):
            print(headers[i].text)
            time.sleep(3)
        rows = self.driver.find_elements_by_xpath(Data.distrows)
        for j in range(len(rows)):
            print(rows[j].text)
            time.sleep(3)
    def tearDown(self):
            footer = self.driver.find_elements_by_xpath(Data.footer)
            for i in range(len(footer)):
                print(footer[i].text)
            time.sleep(5)
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()