#jie cheng

def jie(n):
    s=1
    print n,'! = ',
    while n >= 1:
        s = s*n
        n = n-1
    print s
    
jie(4)