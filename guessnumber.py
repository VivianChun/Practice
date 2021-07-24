import random


n = random.randint(1,10)
	
while True:
	x=input('Please input a number between 1 and 10:')
	
	if int(x) == n:
		print('Good guess!')
		break
	elif int(x) > n:
		print('Guess smaller number')
	else:
		print('Guess bigger number')
