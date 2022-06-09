#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    tmp = a_dictionary.copy()
    for i in tmp.keys():
        tmp[i] *= 2
    return tmp
