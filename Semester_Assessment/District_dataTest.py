import csv
import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains

from Data.Paramters import Data


class Semester_Home(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox(executable_path=Data.fpath)
        time.sleep(3)
        self.driver =webdriver.Chrome(Data.Path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(Data.URL)
        self.driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()
        time.sleep(5)

    def test_Distnames(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(Data.SR).click()
        time.sleep(5)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        time.sleep(5)
        count =len(dots) - 1
        print("no of dots :",count)
        with open('/home/chetan/Documents/Semester/District_wise_report.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)


    def tearDown(self):
        time.sleep(5)
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()