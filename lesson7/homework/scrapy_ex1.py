#!/usr/bin/env python
# encoding: utf-8
"""
@author: Hank zhang
@contract:zhanghao_87@aliyun.com
@file: scrapy_ex1.py
@time: 2016/10/29 22:17
"""
import urllib
from bs4 import BeautifulSoup
import re

url = 'http://www.heibanke.com/lesson/crawler_ex00/'
number = ''
loop = 1
numlist = []
oldnum = ''
while True:
    html = urllib.urlopen(url+number)
    bs_obj = BeautifulSoup(html, 'html.parser')
    content = bs_obj.html.body.div.h3.text
    if not re.search(r'[0-9]+', bs_obj.html.body.div.h3.text) or loop >= 100:
        break
    number = re.findall(r'[0-9]+', bs_obj.html.body.div.h3.text)[0]
    print bs_obj.html.body.div.h3.text, "第%d数字"%loop
    if number == oldnum:
        break
    numlist.append(number)
    loop+=1
    oldnum = number
