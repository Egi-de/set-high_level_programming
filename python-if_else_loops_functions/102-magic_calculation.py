#!/usr/bin/python3
def magic_calculation(a, b, c):
    """Replicates the given bytecode's behavior"""
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c
