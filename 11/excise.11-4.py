print 'time total minutes'

timestr = int(raw_input('Please input total minutes:'))
def trans_hour(arg):
    print 'the time is %d:%d' %(arg/60,arg%60)
    
trans_hour(timestr)