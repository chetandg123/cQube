import time
import unittest

from selenium import webdriver

from Data.Paramters import Data


class Click_ChangePassword(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(Data.Path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(Data.URL)
        self.driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()
        time.sleep(5)

    def test_set_newpwd(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav/div/mat-nav-list/mat-list/mat-list-item/div/button/span/mat-icon").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav/div/mat-nav-list/mat-list/div/a[2]/div/span").click()
        pwd =self.driver.find_element_by_xpath("//h2").text
        self.assertEqual(pwd,"Change Password","Change password is not found!..")
        # self.driver.find_element_by_xpath("//input[@name='newPasswd']").send_keys("1234")
        # time.sleep(2)
        # self.driver.find_element_by_xpath("//input[@name='cnfpass']").send_keys("1234")
        # time.sleep(2)
        # self.driver.find_element_by_xpath("//button[@type='submit']").click()

    def tearDown(self):
            time.sleep(5)
            self.driver.close()

if __name__ == "__main__":
        unittest.main()