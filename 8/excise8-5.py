# yue shu 

from math import sqrt

def getfactors(num):
    factors_list=[]
    t = int(num/2)
    for i in range(t,0,-1):
        if num%i == 0:
            factors_list.append(i)
    factors_list.append(num)
    print factors_list


if __name__ == '__main__':
    getfactors(12)        
