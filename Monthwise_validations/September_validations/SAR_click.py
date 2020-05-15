import time
import unittest

from Data.Paramters import Data
from selenium import webdriver

class SAROption(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(Data.Path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(Data.URL)
        self.driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()
        time.sleep(10)


    def test_SAR(self):
        self.driver.find_element_by_xpath(Data.year).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Data.Sept).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        menu_name=self.driver.find_element_by_xpath("//td[contains(text(),'Student Attendance Reports ')]").text
        print(menu_name)
        # self.assertEqual("   Student Attendance Reports",menu_name,"Not matching!")

        self.driver.find_element_by_xpath(Data.SAR).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(Data.Blocks).click()
        time.sleep(15)
        print("Block details..")
        infob = self.driver.find_elements_by_xpath(Data.details)
        for i in range(len(infob)):
            print(infob[i].text)

        self.driver.find_element_by_xpath(Data.Clusters).click()
        time.sleep(15)
        print("Cluster details..")
        infoc = self.driver.find_elements_by_xpath(Data.details)
        for i in range(len(infoc)):
            print(infoc[i].text)

        self.driver.find_element_by_xpath(Data.Schools).click()
        print("for schools details...")
        time.sleep(15)
        infos = self.driver.find_elements_by_xpath(Data.details)
        for i in range(len(infos)):
            print(infos[i].text)

    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()