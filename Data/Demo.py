

import csv
import time
import unittest

from selenium import webdriver

from Data.Paramters import Data


class Sel_type(unittest.TestCase):
    def setUp(self):
        print("script execution starts...")
        self.driver = webdriver.Chrome(Data.Path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(Data.URL)
        self.driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()
        time.sleep(2)

    def test_select(self):
        dots = self.driver.find_elements_by_xpath(Data.dots)
        count = len(dots)
        print(count)
        self.driver.find_element_by_xpath(Data.Download).click()
        time.sleep(30)
        with open('/home/chetan/Documents/Data_files/District_wise_report.csv', 'r') as file:
            reader = csv.reader(file)
            lines = len(list(reader))
            print(lines)
        self.assertEqual(count,lines,"unmatching count found")
    def tearDown(self):
            time.sleep(5)
            print("script execution ends...")
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()

















# import time
# import unittest
#
# from selenium import  webdriver
#
# class Google(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome(executable_path="/home/chetan/Downloads/chromedriver_linux64/chromedriver")
#
#     def test_google(self):
#         self.driver.get("https://www.google.com/")
#         print(self.driver.get_window_size())
#         print(self.driver.title)
#
#
#     def tearDown(self):
#         time.sleep(5)
#         self.driver.close()
# if __name__ == "__main__":
#     unittest.main()
# from pip._vendor import requests
#
# req = requests.get('http://localhost:8080/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,":",//crumb)', auth=("ChetanDG", "Chetandg143@"))
# print(req.text)