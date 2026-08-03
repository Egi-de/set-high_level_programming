#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for integer in my_list:
        result.append(integer % 2 == 0)
    return result
