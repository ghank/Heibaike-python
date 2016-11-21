# coding:utf-8

# 作业
# 4-1 实现一个finacci函数，能够高效返回随机数n的fibnacci数列。如
# nlist=[randint(1,40) for I in xrange(100)]
# [fib(n) for n in nlist]
#
# 4-2 公交系统的读文件和查找分别改为函数形式。输入起点和终点，返回
# 最少换乘的方案。
#
# 4-3 tictactoe的改进，增加人机对弈。
#
# 思考题
# 4-4 用wxpython，实现井字棋的图形界面。（关注gui可以考虑）
#
# 4-5 用minimax算法提升井字棋的AI

#4-1
import random
import time

def time_cost(f):
    def _f(*arg, **kwarg):
        start = time.clock()
        a=f(*arg,**kwarg)
        end = time.clock()
        print f.__name__,"run cost time is ",end-start
        return a
    return _f

#递归函数
def fibnacci(n):
    assert n > 0, "n需要大于零."
    if n<=2:
        return 1
    else:
        return fibnacci(n-1) + fibnacci(n-2)

def fib_opt(n):
    a, b, i=0, 1, 1
    if n==0:
        return 0
    while i<n:
        a, b=b, a+b #c=a+b;a=b;b=c;
        i+=1
    else:
        return b

def fib_iter():
    a, b=0, 1
    yield a
    while True:
        yield b
        a, b=b, a+b

nlist = [random.randint(1, 40) for I in xrange(1)]
start = time.clock()
for elem in nlist:
    print fibnacci(elem)
end = time.clock()
print end - start
print "------------------------------------"
start = time.clock()
for elem in nlist:
    print fib_opt(elem)
end = time.clock()
print end - start
print "------------------------------------"
A=fib_iter()
start = time.clock()
# for elem in nlist:
A.next(10000)
end = time.clock()
print end - start


#4-2
# import csv
# import re
#
# def readfile(filename):
#     csvfile = open(r'beijing_jt.csv', 'r')
#     reader = csv.reader(csvfile)
#     next(reader)
#     result={}
#
#     while True:
#         try:
#             jt_info = next(reader)
#         except:
#             break
#         station_pattern = (r'(?P<number>[0-9]+)\s(?P<name>\D+)')
#         station_list = []
#         stations = re.findall(station_pattern, jt_info[-1].decode('utf-8'))
#         for tmp in stations:
#             # print tmp[0], tmp[1].strip()
#             station_list.append(tmp[1].strip())
#         result[jt_info[1]] = station_list
#     csvfile.close()
#     return result
#
# def find
#
# if  __name__ == "__main__":
#     while True:
#         start_station, end_station = raw_input(u"请输入你想查询的公交站名：")
#         print start_station, end_station
#
#         for k, v in result.iteritems():
#             if unicode(find_station, 'utf-8') in v:
#                 print k, find_station



#4-3

