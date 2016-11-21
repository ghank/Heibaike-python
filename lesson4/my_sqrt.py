import math

def my_sqrt(num, small_value):
    # if num < 0:
    #     print "num < 0"
    #     return None
    #check input
    assert num > 0 and small_value > 0

    result = num / 2.0
    tmp = 0.0

    while (abs(result**2 - num) > small_value):
        if result**2 - num > 0:
            tmp = result
            result = result / 2.0
        else:
            result = (tmp + result) / 2.0

    return result

if __name__ == "__main__":
    # print my_sqrt(20), math.sqrt(20)
    small_value = 0.0000001
    test_data = [10.0, 23, 25, 2]
    for x in test_data:
        y = my_sqrt(x, small_value)
        assert abs(y**2 -x) < small_value, "Error occur in"+str(x)

    print "pass"
