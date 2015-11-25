number = int(raw_input('Enter a number: '))
print '\n'
l = 0;
m = 1;
print m
for i in range(0,100):
	j = l + m
	l = m
	m = j
	print j
	if j > number:
		break
	elif j == number:
		break
	else:
		continue
