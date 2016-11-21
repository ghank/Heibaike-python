import codecs
f=codecs.open('file_ch.txt', 'w','utf-8')

f.write(u'use python do something\n')
f.write(u'heibanke\n')
f.write(u'study 163\n')
f.close()

#read file
f=codecs.open('file_ch.txt', 'r', 'utf-8')
print f.readline()
print f.readline()
print f.readline()
f.close()

import os
print os.path.exists('file_ch.txt')
os.rename('file_ch.txt', 'file_test.txt')
print os.path.exists('file_ch.txt')