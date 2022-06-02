#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def calculator(argv):
    n = len(argv) - 1
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a == int(argv[0])
    opp == int(argv[1])
    b == int(argv[2])
    if (opp == "+"):
        print("{:d} + {:d} = {:d}".format(a, b, a + b))
    elif (opp == "-"):
        print("{:d} - {:d} = {:d}".format(a, b, a - b))
    elif (opp == "*"):
        print("{:d} * {:d} = {:d}".format(a, b, a * b))
    elif (opp == "/"):
        print("{:d} / {:d} = {:d}".format(a, b, a / b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "main":
    import sys
    calculator(sys.argv)