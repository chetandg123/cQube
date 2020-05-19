import csv
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
        time.sleep(3)
        self.driver.find_element_by_xpath(Data.crc).click()
        time.sleep(30)
        self.driver.find_element_by_xpath("//*[@id='select']/select/option[3]").click()
        time.sleep(5)
        with open("/home/chetan/Downloads/Datafiles/Block_level_CRC_Report (2).csv", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    def tearDown(self):
            time.sleep(5)
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()