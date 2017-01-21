#su shu
from math import sqrt

def isprime(num):
    for i in range(2,int(sqrt(num))+1):
        if num % i == 0:
            return False
    else:
        return True

if __name__ == '__main__':
    print isprime(12)        
# for eachnum in range(10,21):  
    # print eachnum,'is prime',isprime(eachnum)  