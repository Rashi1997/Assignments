# -*- coding: utf-8 -*-
"""
1) simple program to create and print a dictionary 
in the form (val: val*val) that contains a number (between 2 and n)
   Output format : {2: 4, 3: 9, 4: 16, 5: 25, 6:36}   
"""
class assignment_one:
    d=dict()
    n=int(input("Enter a number "))
    for i in range(2,n+1):
        d.update({i:i*i})
    print(d)