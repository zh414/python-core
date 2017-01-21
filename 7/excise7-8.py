#coding:utf-8

db={}
def adpeople():
    people = raw_input('Please input your name:')
    while True:
        name = people
        if name in db:
            people=raw_input('It have this name,Please input another name:')
            continue
        else:
            break
    num=raw_input('Please input your number:')
    db[name]=num
        
def order_by_people():        
    print sorted(db.items())

def order_by_num():
    print sorted(db.items(),key=lambda v:v[1])
    # db_copy={}
    # for i in db:
        # db_copy.update({}.fromkeys(db[i],i))
    # for i in sorted(db_copy.keys()):
        # print db_copy[i],i

CMDS={'a':adpeople,'p':order_by_people,'n':order_by_num}

def showmenu():
    prompt='''
    'A'dd one people's name
    order by 'P'eople.s name
    order by 'N'umber
    
    Enter your choice: 
    '''
    
    while True:
        while True:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError,KeyboardInterrupt,IndexError):
                choice == 'q'
                
            print '\nYour choice is [%s]' % choice
            if choice not in 'apnq':
                print 'Invalid input'
            else:
                break
        if choice == 'q':
            break
        CMDS[choice]()
        
if __name__ == '__main__':
    showmenu()    