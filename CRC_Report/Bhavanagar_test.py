import csv
import time
import unittest

from selenium import webdriver

from Data.Paramters import Data


class Bhavnagar_cluster(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(Data.Path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.driver.get(Data.URL)
        self.driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()
        time.sleep(3)

    def test_crcclick(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(Data.crc).click()
        time.sleep(40)
        dist = self.driver.find_element_by_xpath("//select[@name='myDistrict']/option[contains(text(),' Bhavnagar')]").click()
        disttxt = self.driver.find_element_by_xpath("//select[@name='myDistrict']/option[contains(text(),' Bhavnagar')]").text
        print(disttxt)
        self.assertEqual(" Bhavnagar ",disttxt,"is not selected ")
        time.sleep(5)
        blk = self.driver.find_element_by_xpath("//select[@name='myBlock']/option[contains(text(),' Palitana ')]").click()
        block = self.driver.find_element_by_xpath("//select[@name='myBlock']/option[contains(text(),' Palitana ')]").text
        print(block)
        self.assertEqual(" Palitana ",block,"is not selected ")
        time.sleep(5)
        # clusters =self.driver.find_element_by_xpath(Data.clusterlist)
        # for i in range(len(clusters)):
        #     clusters[i].click()
        # time.sleep(5)
        count = self.driver.find_element_by_xpath("/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-bar-chart/div/div[5]/div[2]/span").text




    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()