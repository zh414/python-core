def safe_open(filename):
	try:
		f = open(filename,'r')
	except:
		f = None
	return f

print safe_open('zss.txt')