#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    n = len(argv)

    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    oper = argv[2]
    b = int(argv[3])

    if oper not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if oper == "+":
        print("{} {} {} = {}".format(a, oper, b, add(a, b)))
    elif oper == "-":
        print("{} {} {} = {}".format(a, oper, b, sub(a, b)))
    elif oper == "*":
        print("{} {} {} = {}".format(a, oper, b, mul(a, b)))
    else:
        print("{} {} {} = {}".format(a, oper, b, div(a, b)))
