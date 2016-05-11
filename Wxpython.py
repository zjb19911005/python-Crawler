#coding=utf-8
#第一个tk程序
import wx#导入wx模块
# app=wx.App()
# frame =wx.Frame(None,-1,'Junior')
# panel= wx.Panel(frame)
# btn =wx.Button(panel,-1,'zhu')
# frame.Show()
# app.MainLoop()


# class MyApp(wx.App):
#     def __init__(self):
#         wx.App.__init__(self)
#     def OnInit(self):
#         self.frame =wx.Frame(parent=None,id=-1,title=u'朱俊波测试',pos=wx.DefaultPosition,size=wx.DefaultSize,style=wx.DEFAULT_FRAME_STYLE,name='frame1')
#         self.SetTopWindow(self.frame)
#         return True
#
# app =MyApp()
# # app.OnInit()手动调用Oninit
# app.MainLoop()#开始时间循环

class ZhuFame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'ZHU',size=(300,200))
        label=wx.StaticText(self,-1,'Helloworld')
app =wx.App()
zframe=ZhuFame()
zframe.Show()
app.MainLoop()