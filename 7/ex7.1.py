#coding:utf-8

db={}
def newuser():
    promt = raw_input('login desired:')
    while True:
        name = promt
        if name in db.keys():
            promt = raw_input('name taken, try another:')
            continue
        else:
            break
    pwd = raw_input('passwd:')
    db[name] = pwd
    
def olduser():
    name = raw_input('login:')
    pwd = raw_input('passwd:')
    passwd = db.get(name)
    if passwd == pwd:
        print 'Welcom back.',name
    else:
        print 'login incorrect.'
        
CMDs = {'n':newuser,'e':olduser}

def showmenu():
    promt = '''
    (N)ew user login
    (E)xisting user login
    (Q)uit
    
    Enter choice:
    '''
    
    while True:
        while True:
            try:
                choice = raw_input(promt).strip()[0].lower()
            except (EOFError,KeyboardInterrupt,IndexError):
                choice == 'q'
            
            print "\nYou picked: [%s]" %choice           
            if choice not in 'neq':
                print "Invalid input"
            else:
                break
                
        if choice == 'q':
            break
        CMDs[choice]()
        print db

if __name__ == '__main__':
    showmenu()       