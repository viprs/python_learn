#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'自动投递简历',
                          size=(800, 600))
        panel = wx.Panel(self, -1)

        # 投递按钮
        self.start_btn = wx.Button(panel, -1, u"开始投递", pos=(20, 20))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.start_btn)
        self.start_btn.SetDefault()

        # 取消投递  按钮
        self.cancel_btn = wx.Button(panel, -1, u"取消", pos=(200, 20))
        self.Bind(wx.EVT_BUTTON, self.OnCancelClick, self.cancel_btn)

        # 状态信息
        self.state_text = wx.StaticText(panel, -1, u"点击开始",
                                        (125, 25))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.state_text)

        # 投递平台
        self.job51 = wx.CheckBox(panel, -1, u"51Job", (35, 60), (150, 20))
        self.job51.SetValue(True)
        self.cjol = wx.CheckBox(panel, -1, u"人才热线", (35, 80), (150, 20))
        self.cjol.SetValue(True)
        self.zhaopin = wx.CheckBox(panel, -1, u"智联招聘", (35, 100), (150, 20))
        self.zhaopin.SetValue(True)

    def OnClick(self, event):
        #self.start_btn.SetLabel(u"停止投递")
        self.state_text.SetLabel(u"正在投递...")
        self.cancel_btn.Show()

    def OnCancelClick(self, event):
        self.cancel_btn.Hide()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    MainFrame().Show()
    app.MainLoop()