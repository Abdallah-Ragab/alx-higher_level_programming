#!/usr/bin/python3

for c in range(90, 64, -1):
    if (c%2 == 0):
        c += 32
    print(chr(c), end="")
