# -*- coding: utf-8 -*-
"""
2) write a simple method in python which takes keyword
 as arguments (example 'name':'x', 'age':12) and print 
 each item using a loop
"""
class assignment_two:
    def keyword_arg(**kwargs):
        for key,value in kwargs.items():
            print(key + '='+ value)
    keyword_arg(name='Hema',age='18')
