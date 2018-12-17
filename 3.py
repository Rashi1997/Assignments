# -*- coding: utf-8 -*-
"""
3) write a simple python code to create two lists. Fist list consists of numbers
 from 1 to 10 and second list consists of characters from a to e.
 Add these two list and print the final list.

"""

class assignment_three:
    list1=list()
    for i in range(1,11):
        list1.append(i)
    str='abcde'
    list2=list(str)
    list3=list1+list2
    print(list3)