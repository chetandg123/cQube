import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains

from Data.Paramters import Data


class Dangs_clusters(unittest.TestCase):
    @classmethod

    def setUp(self):
        self.driver = webdriver.Chrome(Data.Path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(Data.URL)
        print(self.driver.title)
        self.driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()
        time.sleep(10)

    def test_click_on_clusterwise(self):
        self.driver.find_element_by_xpath("//select[@name='myDistrict']/option[contains(text(),'The Dangs')]").click()
        self.driver.find_element_by_xpath("//select[@name='myBlock']/option[contains(text(),' Ahwa ')]").click()
        print("Ahwa block details...")
        time.sleep(3)
        list = self.driver.find_elements_by_xpath(Data.clusterlist)
        for i in range(len(list)):
            list[i].click()
            time.sleep(8)
            dots = self.driver.find_elements_by_class_name(Data.dots)
            count = len(dots) - 1
            school = self.driver.find_element_by_xpath(Data.schoolcount).text
            students = self.driver.find_element_by_xpath(Data.students).text
            # self.assertEqual(count, school, "mismatching record!...")
            print(list[i].text, "No of dots:", count, " ", "No of schools", school, " ", students)

        print("Subir block details...\n")
        self.driver.find_element_by_xpath("//select[@name='myBlock']/option[contains(text(),' Subir ')]").click()
        time.sleep(3)
        list = self.driver.find_elements_by_xpath(Data.clusterlist)

        for i in range(len(list)):
            list[i].click()
            time.sleep(8)
            dots = self.driver.find_elements_by_class_name(Data.dots)
            count = len(dots) - 1
            school = self.driver.find_element_by_xpath(Data.schoolcount).text
            students = self.driver.find_element_by_xpath(Data.students).text
            self.assertEqual(count, school, "mismatching record!...")
            print(list[i].text, "No of dots:", count, " ", "No of schools", school, " ", students)
        time.sleep(10)
        print("\n")
        print("Waghair block details...")
        self.driver.find_element_by_xpath("//select[@name='myBlock']/option[contains(text(),' Waghai ')]").click()
        time.sleep(5)
        for i in range(len(list)):
            list[i].click()
            time.sleep(8)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        count = len(dots) - 1
        school = self.driver.find_element_by_xpath(Data.schoolcount).text
        students = self.driver.find_element_by_xpath(Data.students).text
        # self.assertEqual(count, school, "mismatching record!...")
        print(list[i].text, "No of dots:", count, " ", "No of schools", school, " ", students)
        time.sleep(10)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
