#refound function max and min

def max2(x,y):   #max2=lambda x,y:x if x>y else y
    if x > y:
        return x
    else:
        return y
  
def min2(x,y):   #min2=lambda x,y:x if x<y else y
    if x < y:
        return x
    else:
        return y  

def my_max(list):
    try:
        retval = reduce(max2,list)
    except (ValueError,TypeError), diag:
        retval = str(diag)
    return retval
 
def my_min(list):
    try:
        retval = reduce(min2,list)
    except (ValueError,TypeError), diag:
        retval = str(diag)
    return retval 
    
print my_max([2,5,'a',8])
print my_min([2,5,3,8])       
print max2(4,8)
print min2(4,8)