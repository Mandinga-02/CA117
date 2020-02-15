#!/usr/bin/env python3

import sys

def main():
    s = sys.stdin.readlines()
    for w in s:
        w = w.strip()
        if w.isdigit():
            print("Thank you for " + w)
            break
        else:
            print(w + " is not a number")

if __name__ == '__main__':
    main()
