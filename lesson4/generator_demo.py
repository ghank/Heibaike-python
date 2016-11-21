# coding: utf-8

import time

def time_cost(f):
    def _f(*arg, **kwarg):
        start = time.clock()
        a = f(*arg, **kwarg)
        end = time.clock()
        #print f.__name__, "run cost time is ", end-start
        return a
    return _f

def fib(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

@time_cost
def fib_opt(n):
    a, b, i = 0, 1, 1
    if n == 0:
        return 0
    while i < n:
        a, b = b, a+b
        i += 1
    else:
        return b

def fib_iter():
    a, b = 0, 1
    yield a
    while True:
        yield b
        a, b = b, a+b

# N = 10000
# import time
#
# start = time.clock()
# opt_result = [fib_opt(i) for i in xrange(N)]
# end = time.clock()
# print end-start
#
# print "---------------------------"
# A = fib_iter()
# start = time.clock()
# iter_result = [A.next() for i in xrange(N)]
# end = time.clock()
# print end-start

#------------------------------------------------
import time

def is_in_words(words, answer):
    for word in words:
        if word in answer:
            return True
    else:
        return False

def machine():
    have_talk = []
    good_words = [u'好', u'棒', u'不错', u'good']
    bad_words = [u'不好', u'糟', u'坏', u'差', u'bad']
    s = ''
    while True:
        answer = (yield s)
        if answer is not None:
            #已问过的内容，会存储在have_talk里
            if answer in have_talk:
                s = u"嘿，'%s' 你忘了已经和我说过这句话了吗？"%answer
            elif answer.endswith('?'):
                s = u"轻松一点，少问自己些问题"
            elif is_in_words(good_words, answer):
                s = u"啊哈，这样就好，继续努力吧！"
            elif is_in_words(bad_words, answer):
                s = u"不要那么消极嘛"
            else:
                s = u"我不理解你说的'%s'是什么意思" % answer

            if answer not in have_talk:
                have_talk.append(answer)

if __name__ == "__main__":
    free_talk = machine()
    free_talk.next()
    print u'我是黑板客的小伙伴，我叫板板'
    time.sleep(1)
    print u'今天天气不错，想和我聊些什么吗？'
    while True:
        message = raw_input()
        answer = free_talk.send(message.decode('utf-8'))
        print u"板板说:'"+answer+"'"
        time.sleep(1.5)
        print u"板板说：'你还想聊些什么吗？'"