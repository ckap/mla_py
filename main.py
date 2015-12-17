# this file is largely deprecated, currently
# planned to be replaced by what is called "new.py"


from chk import IntCheck
from chk import ClauseCheck

print "MLA a001"
print "." * 15
print """
Welcome to the Milton Library Assistant.
Please provide a query."""
value = raw_input('''
\t1 - Hello
\t2 - What is this?
\t3 - Can you hear me?
\t4 - asdfiounbawefuo
  >''')

IntCheck(value)
value = int(value)
check = ClauseCheck(value, 2)
print check
if value == 1:
	print "value is one"
if value == 2:
	print "value two received"
if value == 3:
	print "three"
if value == 4:
	print value
	
