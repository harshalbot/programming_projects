user_input = raw_input('Want to find the next immediate prime number? Reply in Y or N: ')

user_input = user_input.lower()

i = 3
a = 2
if user_input is 'y':
	is_prime()
else:
	print('Thank you')


def is_prime(i):
	while i > a :
		if i%a==0 & a!=i:
		 	i += 1
		 	continue
    
  		else: 
  			print(i)
  			i += 1




