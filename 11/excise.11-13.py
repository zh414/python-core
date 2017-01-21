#coding:utf-8
#use the function of reduce complish iteration(deidai)
import time
def mult(x,y):
    return x*y

def mult1(n):    
    return reduce(mult,range(1,n+1))

def mult2(n):
    return reduce(lambda x,y:x*y,range(1,n+1))


def fun(n):
    mult =1
    if n == 0 or n == 1:
        mult = 1
    else:
        mult =  n * fun(n-1)
    return mult
        
def timeit(func,*arg,**kwarg):
    try:
        start = time.clock()
        retval = func(*arg,**kwarg)
        end = time.clock()
        result = (True,retval,end-start)
    except Exception,diag:
        result = (False,str(diag))
    return result

def main():
    funcs=[mult1,mult2,fun]
    vals =[1,2,3,4,5]
    for eachfunc in funcs:
        print '-'*30
        for eachval in vals:
            retval = timeit(eachfunc,eachval)
            if retval[0]:
                print '%s(%s)=' %(eachfunc.__name__,eachval),retval[1]
                print 'The func costs %s secs' % retval[2]
            else:
                print '%s(%s)=Falied' %(eachfunc.__name__,eachval),retval[1]
                
if __name__ == '__main__':
    main()