#!/usr/bin/python3
for i in range(100):
    if i == 99:
        print("{}".format(i))
        break
    print(f"{:02d}".format(i), end=", ")
