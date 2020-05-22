import re
import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains

from Data.Paramters import Data
from Testscripts.login_page import Home_page


class Ahmedabad_amc(unittest.TestCase):
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
        self.driver.find_element_by_xpath("/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[2]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[2]/option[2]").click()
        time.sleep(8)
        amccount = self.driver.find_elements_by_class_name(Data.dots)
        cnt = len(amccount)-1
        print("no of amc dots :",cnt)
        time.sleep(5)
        amc = self.driver.find_elements_by_xpath("/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option")
        time.sleep(3)
        for i in range(len(amc)):
            amc[i].click()
            time.sleep(3)
            dots = self.driver.find_elements_by_class_name(Data.dots)
            count = len(dots)-1
            print(amc[i].text," : ",count)
            time.sleep(3)
        count = len(amc)-1
        time.sleep(2)
        self.assertEqual(cnt, count, " not matching counts ")
    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()











