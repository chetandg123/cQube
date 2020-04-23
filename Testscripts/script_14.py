

import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains

from Testscripts.script_1 import Home_page

#script to Regular User

class Regular_user(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Chrome(executable_path="/home/chetan/Downloads/chromedriver_linux64/chromedriver")
        self.driver =webdriver.Chrome("/home/chetan/Downloads/chromedriver_linux64/chromedriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://cqube.tibilprojects.com")

    def test_start(self):
        print(self.driver.title)
        self.driver.find_element_by_xpath("//a").click()
        time.sleep(10)
        print(self.driver.title)

    def tearDown(self):
        print(self.driver.current_url)
        time.sleep(5)
        # print(self.driver.get_screenshot_as_file(""))
        self.driver.close()

if __name__ == "__main__":
    # unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output="/home/chetan/PycharmProjects/cQube/Reports/script_1.html"))
    unittest.main()
