#coding:utf-8

def backwd(n,i=0):
    if i < n:
        print str[:i+1]
        backwd(n,i+1)
        
def forwd(n,j=0):
    if j > -n:
        print str[j-1:]
        forwd(n,j-1)
        
str = raw_input('Please input a string:')
n = len(str)
backwd(n)
forwd(n)