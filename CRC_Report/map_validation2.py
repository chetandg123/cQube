import csv
import time
import unittest

from selenium import webdriver

from Data.Paramters import Data
class Map_blocks(unittest.TestCase):
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
        time.sleep(40)
        dist = self.driver.find_element_by_xpath("//select[@name='myDistrict']/option[contains(text(),' Banaskantha ')]").click()
        disttxt = self.driver.find_element_by_xpath("//select[@name='myDistrict']/option[contains(text(),' Banaskantha ')]").text
        print(disttxt)
        self.assertEqual(" Banaskantha ",disttxt,"is not selected ")
        time.sleep(5)

        blocks = self.driver.find_elements_by_xpath(Data.blockslist)
        for i in range(len(blocks)):
            blocks[i].click()
            print(blocks[i].text)
            time.sleep(4)
        time.sleep(3)
        xvalues = self.driver.find_elements_by_xpath(Data.xaxis)
        for i in range(len(xvalues)):
            xvalues[i].click()
            time.sleep(3)



    def tearDown(self):

            self.driver.close()

    if __name__ == "__main__":
        unittest.main()