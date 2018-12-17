# -*- coding: utf-8 -*-
"""
9) create a python program which prints the list of square of numbers starting
 from 1 to n where (n=10)
   Output format: [1,4,9,16,25,36,49,64,81,100]
"""
class assignment_nine:
    l=list()
    for i in range(1,11):
        l.append(i*i)
    print(l)
