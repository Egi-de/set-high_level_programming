#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for integer in (my_list or [])[::-1]:
        print(str.format("{}", integer))
