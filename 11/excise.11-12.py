#timeit.py  p285 testit.py

import time

def timeit(func,*arg,**kwarg):
    try:
        start_time = time.clock()
        retval = func(*arg,**kwarg)
        end_time = time.clock()
        result = (True,retval,end_time-start_time)
    except Exception,diag:
        result = (False,str(diag))
    return result

def it():
    funcs = (int,long,float)
    vals = (1234,12.34,'1234','12.34')
    
    for eachfunc in funcs:
        print '*'*20
        for eachval in vals:
            retval = timeit(eachfunc,eachval)
            if retval[0]:
                print '%s(%s)=' %(eachfunc.__name__,'eachval'),retval[1]
                print 'this func costs %s secs' %retval[2]
            else:
                print '%s(%s)=Falied' %(eachfunc.__name__,'eachval'),retval[1]
            
if __name__ == '__main__':
    it()