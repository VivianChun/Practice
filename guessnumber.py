import random
start=input ('please define start number:')
end=input('please define ending number:')
start=int (start)
end=int(end)

n = random.randint(start,end)
count=0
while True:
	count += 1
	x=input('Please input a number between 1 and 100:')
	
	if int(x) == n:
		print('Good guess!')
		print('It is the',count,'times you guessed!')
		break
	elif int(x) > n:
		print('Guess smaller number')
	else:
		print('Guess bigger number')
	print('It is the',count,'times you guessed!')
