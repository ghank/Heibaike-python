#!/usr/bin/env python
# coding: utf-8

# 猜数字
# 改进猜数字游戏，防作弊，错误输入判断

import random

guess, tries = 0, 0
secret = random.randint(1, 100)

while guess != secret and tries < 6:
    guess_str = raw_input(u"请输入一个数字：")
    try:
        guess = int(guess_str)
    except Exception ,e:
        print e
        continue

    if guess == secret:
        print u"猜中了"
    elif guess > secret:
        print u"数字大了"
    else:
        print u"数字小了"
else:
    print "sorry, your times is used off, now"
    print "secert is ", secret


