#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return None
    biggest = my_list[0]
    for x in range(1, len(my_list)):
        if my_list[x] > biggest:
            biggest = my_list[x]
    return biggest
