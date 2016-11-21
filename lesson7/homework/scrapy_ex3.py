#!/usr/bin/env python
# encoding: utf-8
"""
@author: Hank zhang
@contract:zhanghao_87@aliyun.com
@file: scrapy_ex3.py
@time: 2016/11/11 23:38
"""
import urllib
import os
import re

def downloadURL(url):
    if len(url) > 0:
        print "current process id is ", os.getpid()
        content1 = urllib.urlopen(url)
        content = content1.read()
        open(r'hanhan/'+url[-26:], 'a+').write(content)
        print 'downloaded', url

def parseTarget(url):
    urls = []
    con = urllib.urlopen(url).read()
    # *,+,?,用于匹配字符串模式出现一次、多次或未出现的情况。
    # . 用于匹配除换行符外的任意一个单个字符
    pattern = r'<a title=(.*?) href=(.*?)>'
    hrefs = re.findall(pattern, con)

    for href in hrefs:
        urls.append(href[1])
        print href

    return urls

if __name__ == "__main__":
    import multiprocessing as multi

    urls = []
    for i in xrange(7):
        http_url = 'http://blog.sina.com.cn/s/articlelist_1191258123_0_'+str(i+1)+'.html'
        try:
            urls.extend(parseTarget(http_url))
            print "have parse "+str(i)+" pages"
        except:
            print "error, hava parse "+str(i)+" pages"
            break

    pool_num = 8
    pool = multi.Pool(pool_num)
    pool.map(downloadURL, urls)


