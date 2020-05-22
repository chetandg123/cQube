import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains

from Data.Paramters import Data


class Districts(unittest.TestCase):
    @classmethod

    def setUp(self):
        time.sleep(3)
        self.driver = webdriver.Chrome(Data.Path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(Data.URL)
        print(self.driver.title)
        self.driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()
        time.sleep(5)

    def test_click_on_districtnames(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(Data.SR).click()
        time.sleep(5)

        distnames = self.driver.find_elements_by_xpath(Data.Distoptions)
        details = self.driver.find_elements_by_xpath(Data.details)
        for i in range(len(distnames)):
            distnames[i].click()
            time.sleep(6)
            dots=self.driver.find_elements_by_class_name(Data.dots)
            count =len(dots)-1
            school =self.driver.find_element_by_xpath(Data.schoolcount).text
            students=self.driver.find_element_by_xpath(Data.students).text
            print(distnames[i].text, "dots : ", count," ",school," ",students )
            time.sleep(4)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
