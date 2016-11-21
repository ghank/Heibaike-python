import random
import codecs

F = codecs.open('user.txt', 'w', 'utf-8')
user = ['john','mike','ruby','pily']

#a = [random.choice(user), random.randint(0,99999)]
name = random.choice(user)
password = random.randint(0,999999).__str__()
F.write(name+','+password+'\n')
F.close()


# -------------------------------------
charactor = 'adbcdefghijklmnopqrstwxyz01234567'
len_char = len(charactor) - 1
a=[0]*4
a[0] = charactor[random.randint(0, len_char)]
a[1] = charactor[random.randint(0, len_char)]
a[2] = charactor[random.randint(0, len_char)]
a[3] = charactor[random.randint(0, len_char)]

name=''.join(a)

a = [0]*6
a[0] = charactor[random.randint(0, len_char)]
a[1] = charactor[random.randint(0, len_char)]
a[2] = charactor[random.randint(0, len_char)]
a[3] = charactor[random.randint(0, len_char)]
a[4] = charactor[random.randint(0, len_char)]
a[5] = charactor[random.randint(0, len_char)]
password = ''.join(a)

f = open('a.txt', 'w')
f.write(name+','+password+'\n')
f.close()

