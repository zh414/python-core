#coding:utf-8
#用递归向后或向前打印一个字符串

# strings = raw_input('Please input the string:')
# n = len(strings)
# def string(n):
    # if n == 0:
        # pass
    # else:
        # string2=strings[::-1]
        # print string2[n-1]
        # return string(n-1)
    
# if __name__ == '__main__':
    # string(n)
def backview(s,i=0):
    if i < len(s):
        print s[0:i+1]
        backview(s,i+1)
        
def forward(s,j=0):
    if j > -len(s):
        print s[j-1:]
        forward(s,j-1)
        
backview('abcdef')
forward('abcdef')