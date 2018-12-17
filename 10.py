# -*- coding: utf-8 -*-
"""
10) write a program to create a new directory, create a new file, 
list the directory using system commands( use os.system or 
subprocess.check_output module) 

"""
import os
class assignment_ten:
    cmd1='mkdir C:/Users/rasdhar/Desktop/Rashi'
    cmd2='fsutil file createnew kitty.txt 0'
    cmd3='dir /s C:/Users/rasdhar/Desktop/Assignments'
    os.system(cmd1)
    os.system(cmd2)
    os.system(cmd3)