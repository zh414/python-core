#translate a string
#coding:utf-8
import re

# srcstr = raw_input("input what you want to translate:")
# dststr = raw_input("what you want get:")
# str = raw_input("print one string:")

def tr(srcstr,dststr,str,case):
    if case == 1:
        print str.replace(srcstr,dststr)
    if case == 0:
        srcstr = srcstr.lower()
        dststr = dststr.lower()
        print str.replace(srcstr,dststr)
        
if __name__ == '__main__':
    tr('ACX','bcd','ACXfffsssACX',0)
    
