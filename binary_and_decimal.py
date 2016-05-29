def binary_to_decimal(number):
	

def decimal_to_binary(number):
	while number > 0:
		binary = ''
		binary += str(number % 2)
		number = number / 2
	return binary [::-1]


print """
		1. Choose 1 to convert binary into decimal 
		2. Choose 2 to convert decimal into binary

	"""

choice = raw_input("Enter the choice")
number = raw_input("Enter the number")


if choice == 1:
	binary_to_decimal()

elif choice == 2:
	decimal_to_binary()
	
else:
	print "Wrong choice"