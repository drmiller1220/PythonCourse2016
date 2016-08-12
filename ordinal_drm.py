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
				return "%dth" % i
			if i>10 and i<20:
				return "%dth" % i
			if i>20 and i % 10 ==1:
				return "%dst" % i
			if i>20 and i % 10 ==2:
				return "%dnd" % i
			if i>20 and i % 10 ==3:
				return "%drd" % i
			if i>20 and i<99:
				return "%dth" % i
			if i > 100 and int(str(i)[-2:]) / 10==1:
				return "%dth" % i
			if i > 100 and int(str(i)[-2:]) % 10==1:
				return "%dst" % i
			if i > 100 and int(str(i)[-2:]) % 10==2:
				return "%dnd" % i
			if i > 100 and int(str(i)[-2:]) % 10==3:
				return "%drd" % i
			else:
				return "%dth" %i
	except TypeError:
		print "Must enter an integer!"
	except:
		print "Default error detected."
	else:
		print "The function ordinalize has been executed."