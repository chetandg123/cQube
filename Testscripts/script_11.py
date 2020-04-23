
import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains

from Testscripts.script_1 import Home_page

#script to click on clusters and mouse over on it dots

class Cluster_Dots(unittest.TestCase):
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

        def ClickOn_Cluster(self):
            self.driver.find_element_by_xpath("/html/body/app-root/app-map-view/div/div[2]/div[1]/button[2]").click()

        lists = self.driver.find_elements_by_class_name("leaflet-interactive")
        def mouseover(i):
            action = ActionChains(self.driver)
            action.move_to_element(lists[i]).perform()
            time.sleep(5)
            del action

        i = 0
        while i < len(lists):
            mouseover(i)
            i = i + 1

    def tearDown(self):
        print(self.driver.current_url)
        time.sleep(5)
        # print(self.driver.get_screenshot_as_file(""))
        self.driver.close()

if __name__ == "__main__":
    # unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output="/home/chetan/PycharmProjects/cQube/Reports/script_1.html"))
    unittest.main()
