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
        time.sleep(2)

    def test_crcclick(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        head =self.driver.find_element_by_xpath("//td[contains(text(),'CRC Reports ')]").text
        # self.assertEqual(head,"    CRC Reports ","not matching!..")
        self.driver.find_element_by_xpath(Data.crc).click()
        time.sleep(30)
        distnames = self.driver.find_elements_by_xpath(Data.crcdistrict)
        for i in range(len(distnames)):
            distnames[i].click()
            time.sleep(5)
            print(distnames[i].text)
    def tearDown(self):
            time.sleep(5)


    if __name__ == "__main__":
        unittest.main()