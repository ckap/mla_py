def IntCheck(value):								# checks if a value provided by
													# raw_input() is an int or string
    while True:										# force while loop to start
        try:
            value = int(value)						# 'is 1 like 1?' -- joe mccray
            break									# if so, break
        except ValueError:							# if it doesn't work
            print("Input not recognised.")			# let 'em know
            value = raw_input()						# make them redo it

def ClauseCheck(value, n): 							# checks for proper context
	while value == int(value): 						# only activate if IntCheck is valid
		value = int(value)
		if value <= n and value >=1: 				# enforce context
			return True 							# return true on correct context
		else:
			print "Input not recognised."
			return False 							# return false on context failure