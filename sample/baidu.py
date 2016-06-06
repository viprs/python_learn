# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com/"

    def tearDown(self):
        self.driver.quit()

    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium ide")
        time.sleep(5)
        driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE * 4)
        driver.find_element_by_id("su").click()


if __name__ == "__main__":
    unittest.main()
