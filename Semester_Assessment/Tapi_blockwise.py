import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains

from Data.Paramters import Data


class Tapi_blkwise(unittest.TestCase):
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
        time.sleep(10)

    def test_click_on_blockwise(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Data.SR).click()
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[31]").click()
        time.sleep(2)
        list =self.driver.find_elements_by_xpath(Data.blockslist)
        for i in range(len(list)):
            list[i].click()
            time.sleep(8)
            dots = self.driver.find_elements_by_class_name(Data.dots)
            count = len(dots) - 1
            school = self.driver.find_element_by_xpath(Data.schoolcount).text
            students = self.driver.find_element_by_xpath(Data.students).text
            print(list[i].text, "dots : ", count, " ", school, " ", students)
            time.sleep(4)

# "/home/chetan/Documents/Semester/Block_wise_report (5).csv"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
