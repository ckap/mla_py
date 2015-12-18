from checkvals import IntCheck
from checkvals import ClauseCheck
import data

def QuesForm(qstring, astring, n, qval): 
	print "%s" % qstring
	print "%s" % astring
	value = raw_input("  >")
	value = IntCheck(value)
	check = ClauseCheck(value, n, qval)
	return value, check

def QuesOuts(value, qval, out1, out2, out3, out4):
	if value == 1:
		newdata = getattr(data, out1)
		qstring, astring, n, qval, out1, out2, out3, out4 = newdata().DataReport()
		MakeQues(qval)
	if value == 2:
		newdata = getattr(data, out2)
		qstring, astring, n, qval, out1, out2, out3, out4 = newdata().DataReport()
		MakeQues(qval)
	if value == 3:
		newdata = getattr(data, out3)
		qstring, astring, n, qval, out1, out2, out3, out4 = newdata().DataReport()
		MakeQues(qval)
	if value == 4:
		newdata = getattr(data, out4)
		qstring, astring, n, qval, out1, out2, out3, out4 = newdata().DataReport()
		MakeQues(qval)

def MakeQues(qval):
	currentdata = getattr(data, qval)
	qstring, astring, n, qval, out1, out2, out3, out4 = currentdata().DataReport()
	value, check = QuesForm(qstring, astring, n, qval)
	QuesOuts(value, qval, out1, out2, out3, out4)

print "MLA a040"
print "." * 15
print """
Welcome to the Milton Library Assistant.
If you have visited before, please enter your save string.
If you are a new visitor, please enter 'a'.
"""
value = raw_input("  >")
if value == "a":
	MakeQues("I")
else:
	MakeQues(value)