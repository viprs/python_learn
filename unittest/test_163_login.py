# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select



class Login_163(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://mail.163.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def test_login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url + "/")
        self.assertEqual(u"163网易免费邮--中文邮箱第一品牌", driver.title)
        #driver.get("http://163.com/")
        #driver.back()
        try:
            self.assertEqual(u"登  录", driver.find_element_by_id("loginBtn").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("lbNormal").click()
        driver.find_element_by_id("idInput").clear()
        driver.find_element_by_id("idInput").send_keys("zelin_test")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("zelin123456")
        driver.find_element_by_id("loginBtn").click()
        self.assertEqual(u"163网易免费邮--中文邮箱第一品牌", driver.title)
        driver.find_element_by_link_text(u"退出").click()
        for i in range(60):
            try:
                if u"您已成功退出网易邮箱。" == driver.find_element_by_xpath("//body/section/h1").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")


if __name__ == "__main__":
    unittest.main()
