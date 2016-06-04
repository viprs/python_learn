#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
download page: http://tungwaiyip.info/software/HTMLTestRunner.html
"""
import sys
import time
import unittest
from HTMLTestRunner import HTMLTestRunner


class TestMountain(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_it_is_true(self):
        self.assertTrue(1 == 0)
        #self.assertTrue(1 != 0)

    def test_it_is_false(self):
        self.assertFalse(1 == 0)

    def test_single_quote_strings(self):
        self.assertTrue('aaa' == "aaa")

    def test_strip_strings(self):
        self.assertTrue("  aaa   ".strip() == "aaa")
        self.assertTrue("  aaa".lstrip() == "aaa")
        self.assertTrue("aaa   ".rstrip() == "aaa")


def fun_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestMountain))
    return suite

if __name__ == '__main__':
    #res = unittest.TextTestRunner(verbosity=2).run(fun_suite())

    fp = open('./test_result_%s.html' % time.strftime("%Y-%m-%d %H-%M-%S"), 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='百度搜索测试报告',
                            description="测试用例执行情况：")
    runner.run(fun_suite())
    fp.close()
    sys.exit(0)
