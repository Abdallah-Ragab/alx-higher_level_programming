#!/usr/bin/python3

for c in range(90, 64, -1):
    x = 0
    if (c%2 == 0):
        x = 32
    print({}.format(chr(c+x)), end="")
