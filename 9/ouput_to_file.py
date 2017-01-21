import os
filename = raw_input('Enter file name:')
fobj = open(filename,'w')
while True:
    aline = raw_input("Enter a line ('.' to quit):")
    if aline != '.':
        fobj.write('%s%s' % (aline,os.linesep))
    else:
        break
fobj.close()
