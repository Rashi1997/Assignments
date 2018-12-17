# -*- coding: utf-8 -*-
"""
6) create a python script which will write json data to a file, read data from
 the same file and display. write two methods one is for write data and one is 
 for read data. Use try and catch block in both methods.
   (write data example: {'name':'your_name', 'company':'cg'})
"""
import json
class assignment_six:
        
    d={'name':'Rashi Dhar','email':'rashi@gmail.com'}
    def write(data):
        try:
            with open('data.txt', 'w') as outfile:  
                json.dump(data, outfile)
        except Exception as e:
            print(e)
    def read():
        try: 
            with open('data.txt') as json_file:  
                data = json.load(json_file)
                return data
        except Exception as e:
            print(e)
    write(d)
    data=read()
    for k,v in data.items():
        print(k + '=' + v)
