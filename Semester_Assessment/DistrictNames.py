import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains

from Data.Paramters import Data


class Semester_Home(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox(executable_path=Data.fpath)
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
        time.sleep(10)
        distnames = self.driver.find_elements_by_xpath(Data.dnames)
        for i in range(len(distnames)):
            print(distnames[i].click())
            time.sleep(3)
            lists = self.driver.find_elements_by_class_name(Data.dots)
            time.sleep(2)
            count = len(lists)-1
            print( distnames[i].text ,":", count)

    def tearDown(self):
        time.sleep()
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()