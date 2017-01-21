#it's the expand of ex7.1.py
#userpw2.py
#coding:utf-8

from datetime import datetime
import time

db={}
dbt={}

def time_value(user):
#the time's 
    if user not in dbt:
        dbt.setdefault(user,datetime.today())
    else:
        time_value = dbt[user]
        t = datetime.today()-time_value
        try:
            if t.hour<=4:
                print 'You already logged in at:<last_login_timestamp>'
        except:
            print 'You already logged in at:<last_login_timestamp>'
        dbt[user] = datetime.today()

def newuser():
    new_name = raw_input('login desired:')
    while True:
        name = new_name
        if not name.isalnum():
            print 'name error'   
            continue   
        else:            
            if name in db.keys():
                new_name = raw_input('name taken,please input again:')
                continue
            else:
                break
    passwd = raw_input('login password:')
    db[new_name] = passwd
    
def olduser():
    name = raw_input('login name:')
    if name in db: 
        passwd=raw_input('login password:')
        if passwd == db.get(name):
            print 'Welcom back'
            time_value(name)        
        else:
            print 'invalid login!'
    else:
        YN = raw_input('Do you want create a new user?  yes/no : ')
        if YN.lower() == 'y':
            newuser()
        else:
            olduser()
        print '\n'

def deluser():
    name=raw_input('input which one you want delete:')
    if name in db.keys():
        db.pop(name)
    else:
        print 'We have no this user!'    

def show_all_user():
    print db.items()
    
CMDs={'n':newuser,'e':olduser,'d':deluser,'s':show_all_user}

def showmenu():
    prompt = '''
    (N)ewuser
    (E)xisting user
    (D)elete user
    (S)how all user 
    
    Enter your choice:
    '''
    while True: 
        while True:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError,KeyboardInterrupt,IndexError):
                choice == 'q'
                
            print '\nYour choice:[%s]' %choice
            if choice not in 'nedsq':
                print 'Invalid chosse'
            else:
                break 
        if choice == 'q':
            break
        CMDs[choice]() 

        
        
if __name__ == '__main__':
    showmenu()
