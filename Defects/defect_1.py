
import time
import unittest
from select import select

from selenium import webdriver
from selenium.webdriver import ActionChains

from Data.Paramters import Data
from Testscripts.login_page import Home_page

#script to click on home_button

class defect_one(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(Data.Path)
        print("scripts starts ....")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(Data.URL)
        self.driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()

    def test_defect(self):
        dist = self.driver.find_element_by_xpath("//select[@name='myDistrict']/option[contains(text(),'Ahmedabad')]").click()
        blk =self.driver.find_element_by_xpath("//select[@name='myBlock']/option[contains(text(),'Amc')]").click()
        self.driver.find_element_by_xpath("//select[@name='myCluster']/option[contains(text(),'Hathijan')]").click()

        self.driver.find_element_by_xpath(Data.zoom_in).click()

        time.sleep(3)
        print(self.driver.get_screenshot_as_file("/home/chetan/PycharmProjects/cQube/Screenshots/defects/def_1.png"))

        lists =self.driver.find_elements_by_class_name("leaflet-interactive")
        self.assertEqual(len(lists),5,"dots are less then no of schools in map")
        print(len(lists))
    def tearDown(self):
        time.sleep(5)
        self.driver.close()
    print("scripts ends ....")
if __name__ == "__main__":
    unittest.main()

