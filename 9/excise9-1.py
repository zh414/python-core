#filter # kaitou de hang

def filer_line():
    fobj = open('zss.txt','w')
    fobj.write('#jiayou\n')
    fobj.write('come on\n')
    fobj.write('#heheda\n')
    fobj.write('hei#hei\n')
    fobj.close()
    fobj = open('zss.txt','r')
    for eachLine in fobj:
        if eachLine[0] == '#':
            continue
        elif '#' in eachLine:   
            #print eachLine.split('#')[0]
            loc = eachLine.find('#')
            print eachLine[:loc]
        else:
            print eachLine,
    fobj.close()
    
filer_line()