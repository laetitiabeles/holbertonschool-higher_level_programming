#!/usr/bin/python3

def common_elements(set_1, set_2):
    set_3 = set()

    for element in set_1:
        if element in set_2:
            set_3.add(element)
    return set_3
