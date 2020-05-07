import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains

from Data.Paramters import Data


class Schools_button(unittest.TestCase):
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

    def test_click_on_schoolssbtn(self):
        self.driver.find_element_by_xpath(Data.Schools).click()
        lists = self.driver.find_elements_by_class_name(Data.dots)
        count = len(lists)
        print(count)
        time.sleep(20)
        print(self.driver.find_element_by_xpath(
            "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-map-view/div/div[4]/div[1]/span").text)
        print(self.driver.find_element_by_xpath(
            "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-map-view/div/div[4]/div[2]/span").text)
        print(self.driver.find_element_by_xpath(
            "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-map-view/div/div[4]/div[3]/span").text)
        # def mouseover(i):
        #     action = ActionChains(self.driver)
        #     action.move_to_element(lists[i]).perform()
        #     time.sleep(3)
        #     del action
        #
        # i = 0
        # while i < len(lists):
        #     mouseover(i)
        #     i = i + 1

    def tearDown(self):
        time.sleep(3)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
