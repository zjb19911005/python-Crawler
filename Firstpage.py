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
values = {'username': 'zjb19911005', 'password': 'zhu2311829'}
data = url1.urlencode(values)
url = 'http://email.163.com/'
request = url2.Request(url, data)
response = url2.urlopen(request)
print response.read()
