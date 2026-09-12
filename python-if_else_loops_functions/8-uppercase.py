#!/usr/bin/python3
def uppercase(str):
    for char in str:
        n = ord(char)
        if 97 <= n <= 122:
            n -= 32
        print("{:c}".format(n), end="")
    print()
