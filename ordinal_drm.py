def ordinalize(i):
	try:
		if isinstance(i,int):
			if i==1:
				return "1st"
			if i==2:
				return "2nd"
			if i==3:
				return "3rd"
			if i >3 and i<10:
				return "%d th" % i
			if i>11 and i<20:
				return "%d th" % i
			if i>20 and i % 10 ==1:
				return "%d st" % i
			if i>20 and i % 10 ==2:
				return "%d nd" % i
			if i>20 and i % 10 ==3:
				return "%d rd" % i
			print "Input has been successfully ordinalized."
	except TypeError:
		print "Input must be an integer."
	except:
		print "Default error detected."
	else:
		print "The function ordinalize has been executed."