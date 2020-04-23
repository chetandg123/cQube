import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

# script to click on crc reports

class CRC_reports(unittest.TestCase):
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
    def test_crcreports(self):
        self.driver.find_element_by_xpath("//div[@class='col-sm-2']/span").click()
        print(self.driver.title)
        time.sleep(2)
        print(self.driver.get_screenshot_as_file("/home/chetan/PycharmProjects/cQube/Screenshots/crc.png"))
        dist = self.driver.find_element_by_xpath("//select[@name='myDistrict']/option[2]").click()
        print(self.driver.find_element_by_xpath("//select[@name='myDistrict']/option[2]").text)

        blk = self.driver.find_element_by_xpath("//select[@name='myBlock']/option[2]").click()
        print(self.driver.find_element_by_xpath("//select[@name='myBlock']/option[2]").text)
        clus = self.driver.find_element_by_xpath("//select[@name='myCluster']/option[2]").click()
        print(self.driver.find_element_by_xpath("//select[@name='myCluster']/option[2]").text)

        # data = self.driver.find_elements_by_xpath("//div[@class='col-sm-4']/span")
        # print(len(data))
        # for i in range(len(data)):
        #     print(data[i].text)
        # time.sleep(5)

    def tearDown(self):
            time.sleep(5)
            # print(self.driver.get_screenshot_as_file(""))
            self.driver.close()

if __name__ == "__main__":
        # unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output="/home/chetan/PycharmProjects/cQube/Reports/script_1.html"))
        unittest.main()
