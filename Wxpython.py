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

class On_Tool(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'ZHU',size=(300,200))
        panel=wx.Panel(self,-1)
        label=wx.StaticText(panel,-1,'Helloworld',(100,10))#一个坐标表示位置
        label.SetBackgroundColour('black')
        label.SetForegroundColour('white')

        text1=wx.StaticText(panel,-1,'On Tool',(100,50),(160,-1),wx.ALIGN_CENTER)#第二个数字160表示是text的长度
        text1.SetBackgroundColour('green')
        text1.SetForegroundColour('yellow')
        text2=wx.TextCtrl(panel,-1,u"输入你的名字：",(100,50),(130,-1))
        text2.SetInsertionPoint(0)
        png=wx.Image('C:\Users\Administrator.XYZ-PC\Desktop\On Tips\icon.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap()#按钮图片话处理
        self.button=wx.BitmapButton(panel,-1,png,pos = (0,0))
app =wx.App()
frame=On_Tool()
frame.Show()
app.MainLoop()