# display by 25 lines of one pai

import os
def display_by_page():
    file_name = raw_input('Please the file you want to display:')
    f = open(file_name,'r')
    n=0
    for i in f:
        print i,
        n+=1
        if n == 25:    
            n = 0
            os.system('pause')
    f.close()

        

display_by_page()            