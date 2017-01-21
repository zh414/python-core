# total lines
import os

def total_lines():
    file_name = raw_input('Please input one file name:')
    if not os.path.exists(file_name):
        print "sorry ",file_name,'not exist'
    elif not os.path.isfile(file_name):
        print file_name,'is not a file'
    else:
        f = open(file_name,'r')
        allines = f.readlines()
        print len(allines)
        # count = 0
        # for eachline in f:
            # count += 1
        # print count
 
total_lines()