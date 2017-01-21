#name track

import re
list = []
errs=1
n = int(raw_input('Enter total number of names:'))
for i in range(n):
    name = raw_input('Please input name %d :' %i) 
    pattern = re.compile('\((\w+),(\w+)\)')
    if ',' not in name: 
        print 'wrong format...should be Last,First.'  
        print 'you have done this %d time(s) already. Fixing input' %errs  
        errs += 1
        continue
    else:
        name = name.split(',')
    list.append((name[1],name[0]))

print 'The sorted list (by last name) is '
for x in sorted(list):
    print x