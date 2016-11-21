def pow_x(x):
    def echo(value):
        return value**x
    return echo

if __name__ == "__main__":
    lst = [pow_x(2), pow_x(3), pow_x(4)]
    for p in lst:
        print p(2)

