#map and zip

def connect(list1,list2):
    if len(list1) != len(list2):
        print 'two lists is not equal'
    else:
        print map(None,list1,list2)
        print zip(list1,list2)
        
connect([1,2,3],['abc','def','ghi'])
connect([1],[2,3])