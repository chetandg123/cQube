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

    def test_semester(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(Data.SR).click()
        time.sleep(15)
        distnames = self.driver.find_elements_by_xpath(Data.Distoptions)

        lists = self.driver.find_elements_by_class_name(Data.dots)
        def mouseover(i):
            action = ActionChains(self.driver)
            action.move_to_element(lists[i]).perform()
            time.sleep(2)
            del action

        i = 0
        while i < len(lists):
            mouseover(2)
            i = i + 1
        count = len(lists)
        print("No of dots :", count)
        dist = len(distnames)
        print("no of districts :", dist)
        self.assertEqual(dist,count,"both are not matching")
    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()