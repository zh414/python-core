#test the function p285

def testit(func,*nkwargs,**kwargs):
    try:
        retval = func(*nkwargs,**kwargs)
        result = (True, retval)
    except Exception, diag:
        result = (False, str(diag))
    return result
    
def test():
    funcs = (int,long,float)
    vals = (1234,12.34,'1234','12.34')
    
    for eachfun in funcs:
        print '-'*20
        for eachval in vals:
            retval = testit(eachfun,eachval)
            if retval[0]:
                print '%s(%s)' %(eachfun.__name__,'eachval'),retval[1]
            else:
                print '%s(%s) failed:' %(eachfun.__name__,'eachval'),retval[1]
if __name__ == '__main__':
    test()