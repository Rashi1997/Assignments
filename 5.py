# -*- coding: utf-8 -*-
"""
5) create a main python script(for example main.py), create a config script
(config.py). In config.py define four variables(name, age(int), email, company).
import this config script from main.py and print these four variables. 
Assume main.py is your starting script.

"""
import config as cf
def main():
    print(cf.name)
    print(cf.age)
    print(cf.email)
    print(cf.company)

if __name__ == "__main__":
   
   main()

