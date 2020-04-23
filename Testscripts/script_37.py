import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
# script to login function
class Logerror(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Chrome(executable_path="/home/chetan/Downloads/chromedriver_linux64/chromedriver")
        # path is chrome driver.exe file location to be replace here
        self.driver = webdriver.Chrome("/home/chetan/Downloads/chromedriver_linux64/chromedriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://cqube.tibilprojects.com")

    def test_start(self):
        print(self.driver.title)
        self.driver.find_element_by_xpath("//input[@id='exampleInputEmail']").send_keys("tibilsolutions@cqube.com")
        self.driver.find_element_by_xpath("//input[@id='exampleInputPassword']").send_keys("tibil12")
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        print(self.driver.current_url)
        time.sleep(10)
        errormsg = self.driver.find_element_by_xpath("//p").text
        print(errormsg)
    def tearDown(self):
            time.sleep(5)
            # print(self.driver.get_screenshot_as_file(""))
            self.driver.close()


if __name__ == "__main__":
    # unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output="/home/chetan/PycharmProjects/cQube/Reports/script_1.html"))
    unittest.main()
