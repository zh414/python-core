#coding:utf-8

def sco():
    score = int(raw_input("Please input a score:"))
    while score < 0:
        print "Data error"
        score = int(raw_input("Please input a score again:"))
        
    if score < 60:
        print "F"
    elif 60 <= score <69:
        print "D"
    elif 70 <= score < 79:
        print "C"
    elif 80 <= score < 89:
        print "B"
    elif 90 <= score <100:
        print "A"

if __name__ == '__main__' :
    sco()        