#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set()
    result = 0

    for element in my_list:
        if element not in unique_set:
            unique_set.add(element)
            result += element

    return result
