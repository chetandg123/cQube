import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
# script to login function
from Data.Paramters import Data


class Log_Out(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(Data.Path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(Data.URL)
        print(self.driver.title)
        self.driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()

    def test_check(self):
        time.sleep(15)
        print(self.driver.find_element_by_xpath("/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-map-view/div/div[4]/div[2]/span").text)




    def tearDown(self):
            time.sleep(5)
            # print(self.driver.get_screenshot_as_file(""))
            self.driver.close()


if __name__ == "__main__":
    # unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output="/home/chetan/PycharmProjects/cQube/Reports/script_1.html"))
    unittest.main()
