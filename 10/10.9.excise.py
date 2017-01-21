import math,cmath

def safe_sqrt(num):
    try:
        f = math.sqrt(num)
    except ValueError:
        f = cmath.sqrt(num)
    return f

if __name__ == '__main__':
    print safe_sqrt(-2)
    