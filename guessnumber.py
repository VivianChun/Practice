import random


n = random.randint(1,100)
count=0
while True:
	count += 1
	x=input('Please input a number between 1 and 100:')
	
	if int(x) == n:
		print('Good guess!')
		break
	elif int(x) > n:
		print('Guess smaller number')
	else:
		print('Guess bigger number')
	print('It is the',count,'times you guessed!')
