# -*- coding: utf-8 -*-
"""
8) create a python program and list out all the files in your current working
 directory using os.walk module. Prints list of files

"""
import os
class assignment_eight:
    for root, dirs, files in os.walk("C:/Users/rasdhar/Desktop/Assignments", topdown=False):
        for name in files:
            print(name)

