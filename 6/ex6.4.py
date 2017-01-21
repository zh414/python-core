#coding:utf-8
#一个列表模拟队列，先进先出

queue = []

def enQ():
    queue.append(raw_input("Enter a new string:"))
    
def popQ():
    if len(queue) == 0:
        print "Cant not pop from an empty queue."
    else:
        print 'Remove [',`queue.pop(0)`,']'
        
def viewQ():
    print queue
    
CMDs={'e':enQ, 'o':popQ, 'v':viewQ}

def showmenu():
    pr = '''
    (E)nqueue
    p(O)pqueue
    (V)iewqueue
    (Q)uit
    
    Enter a choice: '''
    
    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except (EOFError,KeyboardInterrupt,IndexError):
                choice == 'q'
            
            print "\nYou picked: [%s]" %choice           
            if choice not in 'eovq':
                print "Invalid input"
            else:
                break
                
        if choice == 'q':
            break
        CMDs[choice]()

if __name__ == '__main__':
    showmenu()            
    
