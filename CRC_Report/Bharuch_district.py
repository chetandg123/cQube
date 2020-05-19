import csv
import time
import unittest

from selenium import webdriver

from Data.Paramters import Data


class Bharuch_cluster(unittest.TestCase):
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
        dist = self.driver.find_element_by_xpath("//select[@name='myDistrict']/option[contains(text(),' Bharuch')]").click()
        disttxt = self.driver.find_element_by_xpath("//select[@name='myDistrict']/option[contains(text(),' Bharuch ')]").text
        print(disttxt)
        self.assertEqual(" Bharuch ",disttxt,"is not selected ")
        time.sleep(5)
        blk = self.driver.find_element_by_xpath("//select[@name='myBlock']/option[contains(text(),' Bharuch ')]").click()
        block = self.driver.find_element_by_xpath("//select[@name='myBlock']/option[contains(text(),' Bharuch ')]").text
        print(block)
        self.assertEqual(" Bharuch ",block,"is not selected ")
        time.sleep(5)

        self.driver.find_element_by_xpath("//select[@name='myCluster']/option[contains(text(),' Chhipwad ')]").click()
        clu = self.driver.find_element_by_xpath("//select[@name='myCluster']/option[contains(text(),' Chhipwad ')]").text
        print(clu)
        self.assertEqual(" Chhipwad ",clu,"cluster is not loaded")
        time.sleep(5)
        self.driver.find_element_by_xpath(Data.Download).click()
        time.sleep(5)

        footer = self.driver.find_elements_by_xpath(Data.footer)
        for i in range(len(footer)):
            print(footer[i].text)
            time.sleep(5)
    def tearDown(self):
        with open("/home/chetan/Downloads/Datafiles/School_level_CRC_Report.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()