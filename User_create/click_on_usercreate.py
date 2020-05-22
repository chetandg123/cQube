import time
import unittest

from selenium import webdriver

from Data.Paramters import Data


class Click_create(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(Data.Path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(Data.URL)
        self\
            .driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()
        time.sleep(5)

    def test_userlink(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav/div/mat-nav-list/mat-list/mat-list-item/div/button/span/mat-icon").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav/div/mat-nav-list/mat-list/div/a[1]/div/span").click()
        time.sleep(2)
        header = self.driver.find_element_by_xpath("//h2").text
        self.assertEqual(header,"Create User","Create user not found!..")

    def tearDown(self):
            time.sleep(5)
            self.driver.close()

if __name__ == "__main__":
        unittest.main()