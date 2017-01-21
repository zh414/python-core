# filter 
from random import randint

def leap_year(year):
    if year < 1900 or year > 2016:
        print 'year error'
    elif (year % 100 != 0 and year % 4 == 0) or year % 400 ==0 :
        return year,

year = []        
for i in range(10):
    year.append(randint(1900,2016))
print year
print filter(leap_year,year)

print [n for n in [randint(1900,2016) for i in range(10)] if (n%100 !=0 and n %4==0) or n%400 ==0]