# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time

class Mail163(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://mail.163.com"
    
    def test_mail163(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        for i in range(100):
            try:
                if u"邮箱帐号登录" == driver.find_element_by_id("lbNormal").text:
                    break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        time.sleep(10)
        # ERROR: Caught exception [ERROR: Unsupported command [getElementPositionLeft | 163网易免费邮--中文邮箱第一品牌 | ]]
        driver.find_element_by_id("lbNormal").click()
        # driver.find_element_by_name("email").click()
        driver.find_element_by_name("").clear()
        driver.find_element_by_id(u"auto-id-1466951840733").send_keys("zelin_test")
        driver.find_element_by_class_name(u"j-inputtext dlpwd").clear()
        driver.find_element_by_class_name(u"j-inputtext dlpwd").send_keys("zelin123456")
        driver.find_element_by_id("dologin").click()
        # driver.find_element_by_id("idPlaceholder").click()
        # driver.find_element_by_id("idInput").clear()
        # driver.find_element_by_id("idInput").send_keys("zelin_test")
        # driver.find_element_by_id("pwdInput").clear()
        # driver.find_element_by_id("pwdInput").send_keys("zelin123456")
        # driver.find_element_by_id("loginBtn").click()
        for i in range(60):
            try:
                if "zelin_test@163.com" == driver.find_element_by_id("spnUid").text:
                    break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.assertEqual("zelin_test@163.com", driver.find_element_by_id("spnUid").text)
        self.assertNotEqual(u"163网易免费邮--中文邮箱第一品牌", driver.title)
        driver.find_element_by_link_text(u"退出").click()

    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
