cost = int(raw_input("Enter the cost: "))
amount_given = int(raw_input("Enter the money given: "))
return_amount = amount_given - cost
hundreds=0
fifties=0
twenties=0
tens=0
fives=0
twos=0
ones=0
if return_amount >= 100:
	hundreds=0
	hundreds = return_amount/100
	return_amount = return_amount%100

if return_amount >= 50:
	fifties=0
	fifties = return_amount/50
	return_amount = return_amount%50

if return_amount >= 20:
	twenties=0
	twenties = return_amount/20
	return_amount = return_amount%20

if return_amount >= 10:
	tens=0
	tens = return_amount/10
	return_amount = return_amount%10

if return_amount >= 5:
	fives=0
	fives = return_amount/5
	return_amount = return_amount%5

if return_amount >= 2:
	twos=0
	twos = return_amount/2
	return_amount = return_amount%2

if return_amount >= 1:
	ones=0
	ones = return_amount/1
	return_amount = return_amount%1

print 'Your change in denominations: \n Hundreds(100) : %d \n Fifties(50) : %d \n Twenties(20) : %d \n Tens(10) : %d \n Fives(5) : %d \n Twos(2) : %d \n Ones(1) : %d' % (hundreds,fifties,twenties,tens,fives,twos,ones)