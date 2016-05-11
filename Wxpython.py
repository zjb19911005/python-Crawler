#coding=utf-8
#第一个tk程序
import wx#导入wx模块
import time
class App(wx.App):

    def OnInit(self):
        frame=wx.Frame(parent =None,title='朱俊波个人APP')
        frame.show()
        return True
        raw_input("please ")
app=App()
app.MainLoop()