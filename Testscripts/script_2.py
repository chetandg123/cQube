import time
import unittest

from selenium import webdriver

from Testscripts.script_1 import Home_page

#script to click on block button  and take screenshot
class Blocks(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Chrome(executable_path="/home/chetan/Downloads/chromedriver_linux64/chromedriver")
        self.driver =webdriver.Chrome("/home/chetan/Downloads/chromedriver_linux64/chromedriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://cqube.tibilprojects.com")

    def test_start(self):
        print(self.driver.title)
        self.driver.find_element_by_xpath("//input[@id='exampleInputEmail']").send_keys("tibilsolutions@cqube.com")
        self.driver.find_element_by_xpath("//input[@id='exampleInputPassword']").send_keys("tibil123")
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(10)
        self.driver.find_element_by_xpath("/html/body/app-root/app-map-view/div/div[2]/div[1]/button[1]").click()
        print(self.driver.current_url)
    def tearDown(self):
        time.sleep(5)
        # print(self.driver.get_screenshot_as_file(""))
        self.driver.close()

if __name__ == "__main__":
    # unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output="/home/chetan/PycharmProjects/cQube/Reports/script_1.html"))
    unittest.main()
