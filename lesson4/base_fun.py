X = 9

def f1():
    global X
    # print X
    X = 8
    def f2():
        print "in f1()", X
    f2()
    print "in f1()", X

f1()
print "out f1()", X

if __name__ == "__main__":
    f1()
    print "out f1()", X