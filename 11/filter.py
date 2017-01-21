#coding:utf-8
#normal method## 通用方法写程序，选择奇数可以用列表解析来表示
from random import randint

allterms=[]
for i in range(9):
    allterms.append(randint(1,99))
    
for i in allterms:    # print [n for n in allterms if n%2]
    if i%2:
        print i

#filter method do it    使用filter函数来实现     
print '*'*20
def odd(n):
    return n%2
        
print filter(odd,allterms)

#use lambda      使用filter和lambda的组合来实现
print '#'*20
print filter(lambda n:n%2,allterms)

#one line method
print '$'*20
print [n for n in [randint(1,99) for i in range(9)] if n%2]