#reduce jie average

def average(l):
    try:
        sum = float(reduce(lambda x,y:x+y,l))
        retval = sum/len(l)
    except TypeError,dag:
        retval = str(dag)
    return retval
    
print average([])
print average((1,2,3,4))