# ----------------------------------------------------

import hashlib
f = open('a.txt', 'r')
str = f.readline()
f.close()

a = str.strip().split(',')
name = a[0]
password = a[1]
password = hashlib.md5(password).hexdigest()

f = open('b.txt', 'w')
f.write(name+','+password+'\n')
f.close()
