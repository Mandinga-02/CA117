#!/usr/bin/env python3
import sys

def function():
    pass

def main():
    total = 0
    for i in sys.stdin:
        i = i.split()
        # print(i)
    # for k in i:
        total += len(i)
    print(total)

if __name__ == '__main__':
    main()
