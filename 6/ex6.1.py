#coding:utf-8
#identifier string is legal or not
import string
alpha = string.letters + '_'
data = string.digits
myinput = raw_input("Please input a string:")
if len(myinput) > 1:
    if myinput[0] not in alpha:
        print "invalid string"
    else:
        for i in myinput[1:]:
            if i not in alpha+data:
                print "invalid"
                break
        else:
            print "perfect"
else:
    print "we have 2 strings at least"