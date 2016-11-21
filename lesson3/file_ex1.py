# ----------------------------------------------------

import hashlib


while 1:
    f = open('b.txt', 'a+')
    flag = 0
    print "now, register a new count:"
    username = raw_input("please input username:")

    for eachline in f:
        name_password = eachline.strip().split(',')
        if name_password[0] == username:
            flag = 1
            break

    if flag == 0:
        password = raw_input("please input password:")
        password = hashlib.md5(password).hexdigest()
        f.write(username+','+password+'\n')
    else:
        print "the username is already, now."
    f.close()

