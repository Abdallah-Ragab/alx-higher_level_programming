#!/usr/bin/python3

for c in range(90, 64, -1):
    if (c%2 != 0):
        print(chr(c), end="")
    else:
        print(chr(c+32), end="")
