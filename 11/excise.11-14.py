#coding:utf-8
#fibonaqi  斐波那契数列

def fib(n):
    fibs = [0,1,1]
    if n == 1 or n == 2:
        return 1
    else:
        return n+fib(n-1)

print fib(5)