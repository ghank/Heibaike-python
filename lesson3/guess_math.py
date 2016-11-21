#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

import random

secret = random.randint(1, 100)
guess, tries = 0, 0
print u"如果你猜到它，那说明你真的很幸运。"

while guess != secret and tries < 6:
    guess = input("输入一个数字：")
    if guess == secret:
        print "猜中了"
        break
    elif guess > secret:
        print "数字大了"
    elif guess < secret:
        print "数字小了"
    tries += 1
else:
    print "you lose, times is used off."
    print "secret is ", secret


