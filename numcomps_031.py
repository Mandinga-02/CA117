#!/usr/bin/env python3

import sys

def main():
    # a = [x for x in range(1, n + 1) if x % 3 == 0]
    print("Multiples of 3:",[x for x in range(1, int(n) + 1) if x % 3 == 0])
    print("Multiples of 3 squared:", [x * x for x in range(1, int(n) + 1) if x % 3 == 0])
    print("Multiples of 4 doubled:", [x * 2 for x in range(1, int(n) + 1) if x % 4 == 0])
    print("Multiples of 3 or 4:", [x for x in range(1, int(n) + 1) if x % 3 == 0 or x % 4 == 0])
    print("Multiples of 3 and 4:", [x for x in range(1, int(n) + 1) if x % 3 == 0 and x % 4 == 0])
    print("Multiples of 3 replaced:", [x if x % 3 != 0 else "X" for x in range(1, int(n) + 1)])
    print("Prime:", [x for x in range(2, int(n) + 1) if 0 not in [x%d for d in range(2, x)]])

 n = sys.argv[1]

if __name__ == '__main__':
    main()
