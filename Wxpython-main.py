#coding=utf-8
#第一个wx程序
from wx.py.PyAlaModeTest import App
import wx
__author__ = 'Junior'

class App(wx.App):
    def OnInit(self):
        frame=wx.Frame(parent=None,title='Bar')
        frame.Show
        return True

app=App()
app.MainLoop()
