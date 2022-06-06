#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = my_list[:]
    
    for j, i in enumerate(my_list):
        if i % 2 == 0:
            new[j] = True
        else:
            new[j] = False
    return new
