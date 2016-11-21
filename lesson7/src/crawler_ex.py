#!/usr/bin/env python
# encoding: utf-8
"""
@author: Hank zhang
@contract:zhanghao_87@aliyun.com
@file: crawler_ex.py
@time: 2016/11/12 23:23
"""

import urllib
import os
import re

def downloadURL(url):
    if len(url)>0:
        print "current process id is ", os.getpid()
        content1 = urllib.urlopen(url)
        content = content1.read()
        open(r'hanhan/'+url[-26:], 'a+').write(content)
        print 'downloaded', url

def parseTarget(url):
    urls = []
    con = urllib.urlopen(url).read()
    #
    pattern = r'<a title=(.*?) href="(.*?)">'
    hrefs = re.findall(pattern, con)

    for href in hrefs:
        urls.append(href[1])

    return urls

