#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    l = dir(hidden_4)
    for name in l:
        if name[:2] != "__":
            print(name)
