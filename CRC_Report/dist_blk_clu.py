import time
import unittest

from selenium import webdriver

from Data.Paramters import Data


class Ahmedabad_report(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(Data.Path)
        self.driver.maximize_window()
        # self.driver.implicitly_wait(10)
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
        self.driver.find_element_by_xpath("//select[@name='myDistrict']/option[contains(text(),'Ahmedabad')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//select[@name='myBlock']/option[contains(text(),'Amc')]").click()
        time.sleep(5)
        clu = self.driver.find_elements_by_xpath(Data.clusterlist)
        for i in range(len(clu)):
            clu[i].click()
            time.sleep(6)


    def tearDown(self):
        time.sleep(4)
        footer = self.driver.find_elements_by_xpath(Data.footer)
        for i in range(len(footer)):
            print(footer[i].text)
            time.sleep(5)
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()