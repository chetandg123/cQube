import csv
import time
import unittest

from selenium import webdriver

from Data.Paramters import Data


class Vansada_cluster(unittest.TestCase):
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
        self.driver.find_element_by_xpath(Data.crc).click()
        time.sleep(40)
        dist = self.driver.find_element_by_xpath("//select[@name='myDistrict']/option[contains(text(),' Navsari ')]").click()
        disttxt = self.driver.find_element_by_xpath("//select[@name='myDistrict']/option[contains(text(),' Navsari ')]").text
        print(disttxt)
        self.assertEqual(" Navsari ",disttxt,"is not selected ")
        blk = self.driver.find_element_by_xpath("//select[@name='myBlock']/option[contains(text(),' Vansda ')]").click()
        block = self.driver.find_element_by_xpath("//select[@name='myBlock']/option[contains(text(),' Vansda ')]").text
        print(block)
        self.assertEqual(" Vansda ",block,"is not selected ")
        time.sleep(3)
        self.driver.find_element_by_xpath("//select[@name='myCluster']/option[contains(text(),' Vansda ')]").click()
        clu = self.driver.find_element_by_xpath("//select[@name='myCluster']/option[contains(text(),' Vansda ')]").text
        print(clu)
        self.assertEqual(" Vansda ",clu,"cluster is not loaded")
        time.sleep(5)
        self.driver.find_element_by_xpath(Data.Download).click()
        time.sleep(5)
        count = self.driver.find_element_by_xpath("/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-bar-chart/div/div[5]/div[2]/span").text

        with open("/home/chetan/Downloads/Datafiles/School_level_CRC_Report (3).csv", "r") as file:
            reader = csv.reader(file)
            lines = len(list(reader))
            print("no of records in file:", lines)
        self.assertEqual(count, lines, "unmatching count found")


    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()