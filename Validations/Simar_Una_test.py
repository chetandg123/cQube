
import csv
import time
import unittest

from selenium import webdriver

from Data.Paramters import Data


class Gir_dist_validation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(Data.Path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(Data.URL)
        self.driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()
        time.sleep(10)

    def test_validate_District(self):
        dist = self.driver.find_element_by_xpath("//select[@name='myDistrict']/option[contains(text(),'Gir')]").click()
        blk = self.driver.find_element_by_xpath("//select[@name='myBlock']/option[contains(text(),'Una')]").click()
        clu = self.driver.find_element_by_xpath("//select[@name='myCluster']/option[contains(text(),'Simar Kumar')]").click()

        time.sleep(5)
        self.driver.find_element_by_xpath(Data.Download).click()
        lists = self.driver.find_elements_by_class_name(Data.dots)
        count = len(lists)
        print("no of dots:",count)
        time.sleep(20)
        with open("/home/chetan/Documents/Data_files/Schools_Per_Cluster_report (7).csv", 'r') as file:
            reader = csv.reader(file)
            lines = len(list(reader))
            print("no of records in file:",lines)
        self.assertEqual(count,lines,"unmatching count found")
    def tearDown(self):
            time.sleep(5)
            self.driver.close()

if __name__ == "__main__":
        unittest.main()