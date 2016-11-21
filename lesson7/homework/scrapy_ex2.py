#!/usr/bin/env python
# encoding: utf-8
"""
@author: Hank zhang
@contract:zhanghao_87@aliyun.com
@file: scrapy_ex2.py
@time: 2016/10/30 22:45
"""
import requests
import urllib
from bs4 import BeautifulSoup
import re

# url = 'http://www.heibanke.com/lesson/crawler_ex01/'
# name = ''
# pasword = ''
# while True:
#     html = urllib.urlopen(url)
#     bs_obj = BeautifulSoup(html, 'html.parser')

# params = {'firstname': 'Ryan', 'lastname': 'Mitchell'}
# r = requests.post("http://pythonscraping.com/files/processing.php", data=params)
# print r.text

# params = {'email_addr': 'ryan.e.mitchell@gmail.com'}
# r = requests.post("http://post.oreilly.com/client/o/oreilly/forms/quicksignup.cgi", data=params)
# print r.text
# files = {'uploadFile': open('../files/Python-logo.png', 'rb')}
# r = requests.post("http://pythonscraping.com/pages/processing2.php",files=files)
# print(r.text)

#post方法
url = 'http://www.heibanke.com/lesson/crawler_ex01/'
payload = {'username': 'test', 'password':0}
for n in range(30):
    payload['password'] = n
    content = requests.post(url, payload).text
    pattern = r'<h3>(.*)</h3>'
    result = re.findall(pattern, content)
    print "try enter {}...".format(n), result[0]
    if u'错误' not in result[0]:
        break


