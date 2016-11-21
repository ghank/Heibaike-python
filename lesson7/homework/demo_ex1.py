#!/usr/bin/env python
# encoding: utf-8
"""
@author: Hank zhang
@contract:zhanghao_87@aliyun.com
@file: demo_ex1.py
@time: 2016/11/11 23:22
"""
import requests
import re

def ex01():
    """ 第1关:找密码"""
    url = 'http://www.heibanke.com/lesson/crawler_ex00/'
    num = ''
    while True:
        content = requests.get(url + str(num)).text
        pattern = r'<h3>(.*)</h3>'
        result = re.findall(pattern, content)
        try:
            num = int(
                ''.join(map(lambda n: n if n.isdigit() else '', result[0])))
        except:
            break
        print result[0]
    print result[0]


if __name__ == "__main__":
    ex01()