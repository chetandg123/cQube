import csv
import time
import unittest

from selenium import webdriver

from Data.Paramters import Data


class Vallabnagar_dist(unittest.TestCase):
    def setUp(self):
        time.sleep(3)
        self.driver = webdriver.Chrome(Data.Path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(Data.URL)
        self.driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()
        time.sleep(5)

    def test_validate_schoolrecords(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Data.SR).click()
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[13]").click()
        self.driver.find_element_by_xpath("/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[2]/option[5]").click()

        time.sleep(15)
        self.driver.find_element_by_xpath(Data.Download).click()
        lists = self.driver.find_elements_by_class_name(Data.dots)
        count = len(lists)
        print("no of dots:",count)
        with open('/home/chetan/Documents/Semester/Cluster_wise_report (7).csv', 'r') as file:
            reader = csv.reader(file)
            lines = len(list(reader))
            print("no of records in file:",lines)
        self.assertEqual(count,lines,"unmatching count found")
    def tearDown(self):
            time.sleep(5)
            self.driver.close()

if __name__ == "__main__":
        unittest.main()