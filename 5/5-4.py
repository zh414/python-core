#coding:utf-8
def leap():
    ye=int(raw_input("Please give one year time:"))
    if (ye % 4 == 0 and ye % 100 != 0) or (ye % 4 == 0 and ye % 100 == 0):
        print "This year is leap year"
    else:
        print "This year is common year"
        
if __name__ == '__main__':
    leap()