#def under(str):
#	if len(str) > 10:
#		return str + " That is a nice string."
#	else:
#		return "The string isn't long enough"


#print under("This string?")

#x = "String basics"
#print len(x)

def reverse(str):
	return str[::-1]

print reverse("1234abcd")

def scope(num):
	if num in range(0,10):
		return num
	else:
		return "Number not in range, please try again."

print scope(11)


def upper_case(str):
	count = 0
	if str.upper:
		print count


		