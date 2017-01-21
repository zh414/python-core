#coding:utf-8
#clean the blank of the front and end 

import os 

def clean_file(name):
    print "'n' is create a new file"
    print "'r' means rename the file"
    choice = raw_input('Please input your choice:')
    if choice.strip()[0].lower() == 'n':
        new_file = raw_input('Please input a new file name:')
        ef = open(name,'r')
        nf = open(new_file,'w')
        #allines = map((lambda line:line.strip()),ef)
        allines = [line.strip() for line in ef]
        for eachline in allines:
            nf.write(eachline)
            nf.write(os.linesep)
        ef.close()
        nf.close()
    elif choice.strip()[0].lower() == 'r':
        re_name_file = raw_input('Please input the file name:')
        if os.path.exists(re_name_file):
            os.remove(re_name_file)
        
        ef = open(name,'r')
        rf = open(re_name_file,'w')
        #allines = map((lambda line:line.strip()),ef)
        allines = [line.strip() for line in ef]
        for eachline in allines:
            rf.write(eachline)
            rf.write(os.linesep)
        ef.close()
        rf.close()
        
clean_file('excise.11-7.py')
        
            
        
    
