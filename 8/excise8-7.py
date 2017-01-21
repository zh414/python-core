#perfect data

def isperfect(num):
    perfect_list = []
    for i in range(int(num),0,-1):
        if num % i == 0:
            perfect_list.append(i)
    
    if num == sum(perfect_list):
        return True
    else:
        return False
     
for i in range(20):
    print i,'is perfect data',isperfect(i)
                  