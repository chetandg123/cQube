from selenium import webdriver
class Drivers():
    driver = webdriver.Chrome(executable_path="/home/chetan/Downloads/chromedriver_linux64/chromedriver")
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://cqube.tibilprojects.com/")
