from chk import IntCheck
from chk import ClauseCheck
import data


def QuesForm(qstring, astring, n):			# the abstraction of question formation
	print "%s" % qstring					# print our question string
	print "%s" % astring					# print its possible answers
	value = raw_input("  >")
	value = IntCheck(value)					# toss to IntCheck
	check = ClauseCheck(value, n)			# context checking
	return value, check						# return choice integer

def InterpretData(qstring, astring, n, qval, out1, out2, out3, out4):
	return qstring, astring, n, qval, out1, out2, out3, out4	

print "MLA a020"
print "." * 15
print """
Welcome to the Milton Library Assistant.
If you have visited before, please enter your save string.
If you are a new visitor, please enter 'a'.
"""
value = raw_input("  >")
if value == "a":
	findat = data.I()
	qstring, astring, n, qval, out1, out2, out3, out4 = findat.DataReport()
	value, check = QuesForm(qstring, astring, n)
	if value == 1:
		data = getattr(data, out1)
		#print "made it to 31"
		#print data
		t = data().DataReport()
		#print t
		qstring, astring, n, qval, out1, out2, out3, out4 = InterpretData(*t)
		value, check = QuesForm(qstring, astring, n)

	else:
		print "something fucked up"
	
else:
	print "saves not yet implemented"