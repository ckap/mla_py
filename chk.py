def IntCheck(value):
    while True:
        try:
            value = int(value)		# Try and convert to type int
            break
        except ValueError:			# Error handling for int convert errors
            print("Input not recognised.")
            value = raw_input()
			
def ClauseCheck(value):
	while True:
		if value in ("2", "1"):		# is the value in our domain?
			return True
		else:
			print("Input not recognised.")
			value = raw_input()
			