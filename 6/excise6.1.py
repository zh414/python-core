#coding:utf-8
#identifier string is legal or not
import string,keyword
alpha = string.letters + '_'
data = string.digits
myinput = raw_input("Please input a string:")
if len(myinput) > 0:
    if myinput in keyword.kwlist:
        print "Invalid string it's a keyword"
    elif myinput[0] not in alpha:
        print "invalid string"
    else:
        for i in myinput[1:]:
            if i not in alpha+data:
                print "invalid"
                break
        else:
            print "perfect"
else:
    print "we have 1 strings at least"