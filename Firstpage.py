# coding=utf-8
__author__ = 'Junior'
import urllib2 as url2
import urllib as url1
import re

#常规传参
# request=url.Request('http://www.baidu.com/s?cid=qb7.zhuye&ie=utf-8&wd=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80')
# response=url.urlopen(request)
# print response.read()
# news=re

#POST请求
# header={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 QQBrowser/3.9.3943.400'}
# values = {'username': 'zjb19911005', 'password': 'zhu2311829'}
# data = url1.urlencode(values)
# url = 'http://email.163.com/'
# request = url2.Request(url, data,header)
# response = url2.urlopen(request)
# print response.read()

# import urllib2
#
# req = urllib2.Request('http://blog.csdn.net/cqcre')
# #异常捕获
# try:
#     urllib2.urlopen(req)
# except urllib2.HTTPError,e:
#     if hasattr(e,'code'):
#     #判断错误属性是否正确
#         print e.code
# except urllib2.URLError,e:
#     if hasattr(e,'reason'):
#         print e.reason
# else:
#     print 'OK'

#
# import cookielib
# import urllib2
#
# #设置保存cookie的文件,同级目录下的cookie.txt
# filename='/Users/Junior.Zhu/Desktop/cookie.txt'
# #声明一个MozillaCookieJar对象实例来保存cookie,之后写入文件
# cookie=cookielib.MozillaCookieJar(filename)
# #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler =urllib2.HTTPCookieProcessor(cookie)
# #通过handler来构建opener
# opener =urllib2.build_opener(handler)
# #创建一个请求,原理同urllib2的urlopen
# response =opener.open('http://www.baidu.com')
# #保存cookie到文件
# cookie.save(ignore_discard=True,ignore_expires=True)


#利用cookie来登录系统
# import re
# import urllib2
# import cookielib
# filename='/Users/Junior.Zhu/Desktop/cookie.txt'
# #声明一个MozillaCookieJar对象实例来保存cookie,之后写人文件
# cookie =cookielib.MozillaCookieJar(filename)
# opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# #post传参
# postdata=url1.urlencode({'account':'zhujb','password':'123456'})
#
# #登陆禅道系统
# loginUrl='http://zentao.shishike.com/index.php?m=user&f=login'
# #模拟登陆,保存cookie
# response1=opener.open(loginUrl,postdata)
# #保存cookie到cookie.txt中
# cookie.save(ignore_expires=True,ignore_discard=True)
# #利用cookie访问测试专属模块
# testUrl='http://zentao.shishike.com/index.php?m=bug&f=browse'
# response2=opener.open(testUrl)
# print response2.read()

import re
import urllib
import urllib2
request=urllib2.Request('http://www.baidu.com/s?cid=qb7.zhuye&ie=utf-8&wd=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80')
response=urllib2.urlopen(request)
html=response.read()
#print html
news=re.compile(".+?\.王者荣耀.+?\.",re.S)
newslist=re.findall(news,html)
print newslist