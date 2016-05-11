#coding=utf-8
#第一个tk程序
import wx#导入wx模块
# app=wx.App()
# frame =wx.Frame(None,-1,'Junior')
# panel= wx.Panel(frame)
# btn =wx.Button(panel,-1,'zhu')
# frame.Show()
# app.MainLoop()
class MyApp(wx.App):
    def __init__(self):
        wx.App.__init__(self)
    def OnInit(self):
        self.frame =wx.Frame(parent=None,title=u'朱俊波测试')
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

app =MyApp()
app.OnInit()
app.MainLoop()#开始时间循环