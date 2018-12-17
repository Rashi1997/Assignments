# -*- coding: utf-8 -*-
"""
7) create a python script and use argparse module for developing a math 
application using command line inputs. Write four methods 'add', 'sub',
'div', 'mul'. when user inputs -a return addition of two numbers, -s returns
 subtraction of two numbers , -d returns division of two numbers and 
 -m returns multiplication of two numbers

"""
import argparse

parser = argparse.ArgumentParser(description="Calculator")
parser.add_argument('-a', 
                    dest='add', 
                    type=str, 
                    help='Addition')

parser.add_argument('-s', 
                    dest='sub',
                    type=str, 
                    help='Substraction')

parser.add_argument('-d', 
                    dest='div',
                    type=str, 
                    help='Division')
parser.add_argument('-m', 
                    dest='mul',
                    type=str, 
                    help='Multiplication')

args = parser.parse_args()

def addition(a,b):
    print (a + b)

def substraction(a,b):
    print (a - b)
def division(a,b):
    print (a / b)
def multiplication(a,b):
    print (a * b)
    
def main():
    print(args)
    if args.add=='add':
        addition(3,5)
    elif args.sub=='sub':
         substraction(3,5)
    elif args.div=='div':
        division(3,5)
    elif args.mul=='mul':
        multiplication(3,5)
        
main()
