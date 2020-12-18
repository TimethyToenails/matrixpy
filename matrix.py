import random

str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '_', '+', '!', '"', '£', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', ';', ':', '@', '~', '#', '', ',', '.', '<', '>', '?', '/', '|', '`', '¬', '¦', ]

while(True):
	for i in range(230):
		if random.random() > float('0.83'):
			random_num = random.choice(str_list)
			print(random_num, end='')
		else:
			print(' ', end='')			
	print()