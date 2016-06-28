# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest, time

class Duorou(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie(r"C:\Program Files\Internet Explorer\IEDriverServer.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "http://duorou.51tests.net"
    
    def test_duorou(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url + "/Admin/Public/login.html")
        for i in range(60):
            try:
                if u"管理后台" == driver.find_element_by_css_selector("h3.welcome").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.assertEqual(u"管理后台", driver.find_element_by_css_selector("h3.welcome").text)
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("admin")
        time.sleep(1)
        driver.find_element_by_name("username").send_keys("xxx")
        time.sleep(1)
        driver.find_element_by_name("username").send_keys(Keys.SPACE)
        time.sleep(1)
        driver.find_element_by_name("username").send_keys(Keys.BACK_SPACE * 4)
        time.sleep(1)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_css_selector("button.login-btn").click()
        for i in range(60):
            try:
                if u"系统信息" == driver.find_element_by_css_selector("h5").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_link_text(u"商城设置").click()
        time.sleep(3)
        driver.find_element_by_link_text(u"统计分析").click()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.forward()
        time.sleep(3)
        driver.refresh()
        time.sleep(3)
        #driver.find_element_by_class_name("").click()
        #driver.find_element_by_link_text(u"退出").click()
        driver.get(self.base_url + "/Admin/Public/logout.html")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
