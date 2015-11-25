number = int(raw_input("Enter a number: "))

divisible = []
divisible_and_prime = []


def divisible_by_all_numbers():
	for i in range(2,number):
		if number%i==0:
			divisible.append( number )
			
length_divisible = len(divisible)
print divisible

def check_if_prime():
	for j in range(2,length_divisible):
		for k in range(0,length_divisible):
			if divisible[k] % j == 0 & j!= divisible[k]:
				divisible_and_prime.append(divisible[k])

def main():
	divisible_by_all_numbers();

	check_if_prime();

	print 'Prime factors of {0} are {1}'.format(number, divisible_and_prime)

main()
