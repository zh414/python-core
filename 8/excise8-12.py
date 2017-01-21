# input and output format

def string_format(begin_num,end_num):
    for x in xrange(begin_num,end_num):
        if 32<x<127:
            print 'DEC\tBIN\tOCT\tHEX\tASCII'
            print '-'*40  
            break
    print 'DEC\tBIN\tOCT\tHEX'
    # if begin_num<127 or end_num <32: 要看清结合的分类及节点
        # print 'DEC\tBIN\tOCT\tHEX'
        # print '-'*30
    # else:
        # print 'DEC\tBIN\tOCT\tHEX\tASCII'
        # print '-'*40 
    for x in xrange(begin_num,end_num+1):
        if 32<x<127:
            print '%d\t%d\t%o\t%x\t%c' %(x,int(bin(x)[2:]),x,x,x)
        else:
            print '%d\t%d\t%o\t%x\t' %(x,int(bin(x)[2:]),x,x)

string_format(9,32)

