import time
import unittest

from selenium import webdriver

from Data.Paramters import Data


class Navsari_cluster(unittest.TestCase):
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
        time.sleep(5)
        self.driver.find_element_by_xpath(Data.crc).click()
        time.sleep(40)
        dist = self.driver.find_element_by_xpath("//select[@name='myDistrict']/option[contains(text(),'Navsari')]").click()
        disttxt = self.driver.find_element_by_xpath("//select[@name='myDistrict']/option[contains(text(),'Navsari')]").text
        print(disttxt)
        self.assertEqual(" Navsari ",disttxt,"is not selected ")
        time.sleep(5)
        blk = self.driver.find_element_by_xpath("//select[@name='myBlock']/option[contains(text(),'Gandevi')]").click()
        block = self.driver.find_element_by_xpath("//select[@name='myBlock']/option[contains(text(),'Gandevi')]").text
        print(block)
        self.assertEqual(" Gandevi ",block,"is not selected ")
        time.sleep(5)

        self.driver.find_element_by_xpath("//select[@name='myCluster']/option[contains(text(),' Amalsad ')]").click()
        clu = self.driver.find_element_by_xpath("//select[@name='myCluster']/option[contains(text(),' Amalsad ')]").text
        print(clu)
        self.assertEqual(" Amalsad ",clu,"cluster is not loaded")
        time.sleep(5)
        self.driver.find_element_by_xpath(Data.Download).click()
        time.sleep(5)
        headers = self.driver.find_elements_by_xpath(Data.headers)
        for i in range(len(headers)):
            print(headers[i].text)
            time.sleep(3)

        rows = self.driver.find_elements_by_xpath(Data.distrows)
        for j in range(len(rows)):
            print(rows[j].text)
            time.sleep(5)
        footer = self.driver.find_elements_by_xpath(Data.footer)
        for i in range(len(footer)):
            print(footer[i].text)
            time.sleep(5)
    def tearDown(self):

            self.driver.close()

    if __name__ == "__main__":
        unittest.main()