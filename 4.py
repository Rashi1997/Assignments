# -*- coding: utf-8 -*-
"""
4) write a simple class with constructor which takes two integer arguments(a,b).
 Write a method inside class as get_sum(), which returns the sum of (a and b).
 Prints the sum

"""
class assignment_four:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def get_sum(self):
        print("The sum of {} and {}  is {}".format(self.a,self.b,self.a+self.b))
inst=assignment_four(3,5)
inst.get_sum()
