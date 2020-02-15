#!/usr/bin/env python3

import sys

def reverse(s):
    return s[::- 1]

def palindrome(s):
    """ Check if the string reads the same backward"""
    if s == reverse(s):
        return True
    return False

def main():
    for i in sys.stdin:
        a = i.strip().lower().split()
        b = "".join(a)
        n_str = ""
        for k in b:
            if k.isdigit() or k.isalpha():
                n_str += k
        print(palindrome(n_str))
        # print(n_str)
if __name__ == '__main__':
    main()
