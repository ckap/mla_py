_data = {}
class I:
	def DataReport(self):
		qstring = "\nWelcome, Guest.  Please enter a query."
		astring = """\t 1 - Hello.
\t 2 - Can you hear me?
\t 3 - \\list
\t 4 - afaskjhfskjfhsf"""
		n = 4
		qval = "I"
		out1 = "II"
		out2 = "IG"
		out3 = "IV"
		out4 = "IJ"
		return qstring, astring, n, qval, out1, out2, out3, out4

class II:
	def DataReport(self):
		qstring = """\nHello, Guest.  Unfortunately, your query is quite limited.  Please elaborate."""
		astring = """\t 1 - Elaborate? \n\t 2 - What is this thing? \n\t 3 - \\help \n\t 4 - How are you?"""
		n = 4
		qval = "II"
		out1 = "III"
		out2 = "IIG"
		out3 = "IIV"
		out4 = "IIJ"
		return qstring, astring, n, qval, out1, out2, out3, out4