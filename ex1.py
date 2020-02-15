#!/usr/bin/env python3

import sys
import string
def main():
    lst = []
    for line in sys.stdin.read():
        new = ""
        for l in line:
            if l.isalnum():
                new += l
            if l == " ":
                new = new.lower()
                if new not in lst:
                    lst.append(new)
                
    print(len(lst))




    

if __name__ == '__main__':
    main()
