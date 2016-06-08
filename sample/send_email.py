#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = u'zelin_test@163.com'
receivers = [u'zelin_test@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

MAIL_SERVER = 'stmp.163.com'
MAIL_USERNAME = "zelin_test"
MAIL_PASSWORD = "Zelin123456" #设置的第三方授权码

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
MAIL_TEXT = u"""
<HTML>
<HEAD>
<TITLE>
自动化测试邮件报告
</TITLE>
</HEAD>
<BODY>
Python 邮件发送测试..
</BODY>
</HTML>
"""
message = MIMEText(MAIL_TEXT, 'html', 'utf-8')

subject = u'Python SMTP 自动化测试邮件'
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect("smtp.163.com")
    smtpObj.login(MAIL_USERNAME, MAIL_PASSWORD)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print u"邮件发送成功"
except smtplib.SMTPException as e:
    print e