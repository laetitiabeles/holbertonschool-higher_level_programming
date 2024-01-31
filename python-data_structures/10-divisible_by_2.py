#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for index in my_list:
        if index % 2 == 0:
            new_list[index] = True
        else:
            new_list[index] = False
    return new_list