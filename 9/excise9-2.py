# show define lines

def show():
    n=int(raw_input('Please input the number N:'))
    file_name=raw_input('Please input which file you want to open:')
    f = open(file_name,'r')
    for i in range(n):
        print f.next(),
    
show()