#!/usr/bin/python3
def add_args(argv):


    n = len(argv) - 1
    if n == 0:
        print("{:d}".format(n))
        return
    else:
        i = 1
        sum = 0
        while i <= n:
            sum += int(argv[i])
            i += 1
        print("{:d}".format(sum))


if __name__ == "__main__":
    import sys
    add_args(sys.argv)
