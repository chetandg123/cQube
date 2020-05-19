import time
import unittest

from selenium import webdriver

from Data.Paramters import Data


class XYaxis(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(Data.Path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(Data.URL)
        self.driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()
        time.sleep(2)

    def test_click_xyaxis(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        head =self.driver.find_element_by_xpath("//td[contains(text(),'CRC Report ')]").text
        self.driver.find_element_by_xpath(Data.crc).click()
        time.sleep(20)
        xaxis_lists =self.driver.find_elements_by_xpath(Data.xaxis)
        yaxis_lists = self.driver.find_elements_by_xpath(Data.yaxis)
        for i in range(len(xaxis_lists)):
            xaxis_lists[i].click()
            print(xaxis_lists[i].text)
            time.sleep(4)
            for j in range(len(yaxis_lists)):
                yaxis_lists[i].click()
                print(yaxis_lists[j].text)
                time.sleep(4)



    def tearDown(self):
            time.sleep(5)
            self.driver.close()

if __name__ == "__main__":
        unittest.main()