import csv
import time
import unittest

from Data.Paramters import Data
from selenium import webdriver

class Amreli_district(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(Data.Path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(Data.URL)

    def test_clusterbtn(self):
        print(self.driver.title)
        self.driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(Data.SR).click()
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[25]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[2]/option[2]").click()
        time.sleep(8)
        self.driver.find_element_by_xpath("/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option[2]").click()
        time.sleep(5)
        amccount = self.driver.find_elements_by_class_name(Data.dots)
        cnt = len(amccount)-1
        print("no of dots :",cnt)
        with open('/home/chetan/Documents/Semester/School_wise_report (5).csv', 'r') as file:
            reader = csv.reader(file)
            # for row in reader:
            #     print(row)
            lines = len(list(reader))-1
            print("no of records in file:", lines)
        self.assertEqual(cnt,lines,"dots are not matching")
    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

