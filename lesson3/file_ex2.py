#!/usr/bin/env python
# coding: utf-8

import hashlib
import re

while True:
    flag = True
    print "now, register a new count."

    username = raw_input("please input username:")
    result = re.match(r'\b[a-zA-Z][-\w]+', username)
    print result
    if result == None:
        print u"username 格式不对"
        flag = False
    elif len(username) < 4:
        print u"username 长度不够"
        flag = False
    else:
        flag = True

    if flag:
        f = open('b.txt', 'r')
        for eachline in f:
            name_password = eachline.strip().split(',')
            if name_password[0] == username:
                print "the username is already, now."
                flag = False
                break
        f.close()

    if not flag:
        continue

    password = raw_input("please input password:")
    result = re.match(r'[-\w]+', password)
    if result == None:
        print u"password 格式不对"
        flag = False
    elif len(password) < 6:
        print u"password 长度不够"
    else:
        flag = True

    if flag:
        f = open('b.txt', 'a+')
        password = hashlib.md5(password).hexdigest()
        f.write(username+','+password+'\n')
        f.close()

