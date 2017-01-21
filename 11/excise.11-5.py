#cacular your tax

sales = float(raw_input('Please input your sales:'))
def tax(sale,rate=0.05):
    print 'your tax is %s' %(sale*rate)
    
tax(sales)
tax(sales,0.01)