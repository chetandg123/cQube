
import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains

from Data.Paramters import Data
from Testscripts.login_page import Home_page


#mouse over on dots in homePage

class Home_Dots(unittest.TestCase):
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

    def test_dotsover(self):

        lists = self.driver.find_elements_by_class_name(Data.dots)
        def mouseover(i):

            action = ActionChains(self.driver)
            action.move_to_element(lists[i]).perform()
            time.sleep(3)
            del action


        i = 0
        while i < len(lists):
            mouseover(i)
            i = i + 1


    def tearDown(self):
        time.sleep(5)
        # print(self.driver.get_screenshot_as_file(""))
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
