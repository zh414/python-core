# yue shu 

from math import sqrt

def isprime(num):
    for i in range(2,int(sqrt(num))+1):
        if num % i == 0:
            return False
    else:
        return True
        
def getfactors(num):
    factors_list=[]
    t = int(num/2)
    for i in range(2,t):
        if isprime(i) and num%i == 0:
            factors_list.append(i)
            num = num / i
            t = num /2
    if num != 1:
        factors_list.append(num)
    print factors_list


if __name__ == '__main__':
    getfactors(20)        
