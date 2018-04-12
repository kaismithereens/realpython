from random import randint

number = 0

for simulation in range(1,10001):
	number = number + randint(1,6)

print("The average number is:", number/10000)