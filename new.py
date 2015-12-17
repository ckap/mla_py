from chk import IntCheck
from chk import ClauseCheck

def QuesForm(qstring, astring, n):			# the abstraction of question formation
	print "%s" % qstring					# print our question string
	print "%s" % astring					# print its possible answers
	value = raw_input("  >")
	IntCheck(value)							# toss to IntCheck
	value = int(value)
	check = ClauseCheck(value, n)			# context checking
	return int(value)						# return choice integer

print "MLA a001"
print "." * 15
print """
Welcome to the Milton Library Assistant.
If you have visited before, please enter your save string.
If you are a new visitor, please enter 'a'.
"""
value = raw_input("  >")
if value == "a":
	QuesForm("This is the question", "These are the answers", 4)
	print "result"
else:
	print "saves not yet implemented"