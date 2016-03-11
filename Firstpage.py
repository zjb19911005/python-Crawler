#coding=utf-8
__author__ = 'Junior'
import requests as req
import re

html=req.get('http://www.baidu.com/')
print html.text