def IntCheck(value):
    while True:
        try:
            value = int(value)
            return value
        except ValueError:
            print "Input not recognised."
            value = raw_input("  >")

def ClauseCheck(value, n, qval):
	while True:
	   if value <= n and value >=1:
	       return True
	   else:
	       print """Input not recognised. Program will likely crash here. \
Your save string is '%s'""" % qval
	       value = raw_input("  >")
	       value = IntCheck(value)