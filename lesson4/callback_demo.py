def test(callback):
    print 'test func begin'
    callback()
    print 'test func end'

def cb1():
    print 'callback 1'

def cb2():
    print 'callback 2'

test(cb1)
test(cb2)