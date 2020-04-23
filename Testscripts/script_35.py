import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

# script to choose district , block ,cluster and mouse over on last

class Choose20(unittest.TestCase):
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
        print(self.driver.current_url)
        time.sleep(10)


        dist = self.driver.find_element_by_xpath("//select[@name='myDistrict']/option[20]").click()
        print(self.driver.find_element_by_xpath("//select[@name='myDistrict']/option[20]").text)

        blk = self.driver.find_element_by_xpath("//select[@name='myBlock']/option[3]").click()
        print(self.driver.find_element_by_xpath("//select[@name='myBlock']/option[3]").text)
        clus= self.driver.find_element_by_xpath("//select[@name='myCluster']/option[8]").click()
        print(self.driver.find_element_by_xpath("//select[@name='myCluster']/option[8]").text)

        data = self.driver.find_elements_by_xpath("//div[@class='col-sm-4']/span")
        print(len(data))
        for i in range(len(data)):
            print(data[i].text)
        time.sleep(5)

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
            time.sleep(5)
            # print(self.driver.get_screenshot_as_file(""))
            self.driver.close()

if __name__ == "__main__":
        # unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output="/home/chetan/PycharmProjects/cQube/Reports/script_1.html"))
        unittest.main()
