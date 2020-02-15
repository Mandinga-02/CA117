#!/usr/bin/env python3

import sys
import calendar
m = "Monday's child is fair of face."
t = "Tuesday's child is full of grace."
w = "Wednesday's child is full of woe"
th = "Thursday's child has far to go."
f = "Friday's child is loving and giving."
s = "Saturday's child works hard for a living."
su = "Sunday's child is fair and wise and good in every way."

def birthday(day, month, year):
    day = calendar.weekday(year, month, day)
    if int(day) == 0:
        return "You were born on a Monday and {:s}".format(m)
    if int(day) == 1:
        return "You were born on a Tuesday and {:s}".format(t)
    if int(day) == 2:
        return "You were born on a Wednesday and {:s}".format(w)
    if int(day) == 3:
        return "You were born on a Thursday and {:s}".format(th)
    if int(day) == 4:
        return "You were born on a Friday and {:s}".format(f)
    if int(day) == 5:
        return "You were born on a Saturday and {:s}".format(s)
    if int(day) == 6:
        return "You were born on a Sunday and {:s}".format(su)

def main():
    day = sys.argv[1]
    month = sys.argv[2]
    year = sys.argv[3]
    print(birthday(int(day), int(month), int(year)))

if __name__ == '__main__':
    main()
