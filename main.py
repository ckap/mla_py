from chk import IntCheck
from chk import ClauseCheck

print "MLA a001"
print "." * 15
print "Are you a boy or a girl?"
value = raw_input('''
\t 1 - male
\t 2 - female\n''')
IntCheck(value)
check = ClauseCheck(value)
