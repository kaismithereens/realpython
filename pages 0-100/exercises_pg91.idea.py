#How many times the die has fallen on each number in 10000 roles

from random import randint

number_1 = 0
number_2 = 0
number_3 = 0
number_4 = 0
number_5 = 0
number_6 = 0

for simulation in range(1,10001):
	number = randint(1,6)
	if number == 1:
		number_1 = number_1 + 1
	elif number == 2:
		number_2 = number_2 + 1
	elif number == 3:
		number_3 = number_3 + 1
	elif number == 4:
		number_4 = number_4 + 1
	elif number == 5:
		number_5 = number_5 + 1
	else:
		number_6 = number_6 + 1

print(f"Number 1 has been tossed {number_1} times")
print(f"Number 2 has been tossed {number_2} times")
print(f"Number 3 has been tossed {number_3} times")
print(f"Number 4 has been tossed {number_4} times")
print(f"Number 5 has been tossed {number_5} times")
print(f"Number 6 has been tossed {number_6} times")

if number_1 > number_2 and number_1 > number_3 and number_1 > number_4 and number_1 > number_5 and number_1 > number_6:
	print("Number 1 has been tossed the most times")
elif number_2 > number_3 and number_2 > number_4 and number_2 > number_5 and number_2 > number_6:
	print("Number 2 has been tossed the most times")
elif(number_3 > number_4) and (number_3 > number_5) and (number_3 > number_6):
	print("Number 3 has been tossed the most times")
elif(number_4 > number_5) and (number_4 > number_6):
	print("Number 4 has been tossed the most times")
elif(number_5 > number_6):
	print("Number 5 has been tossed the most times")
else:
	print("Number 6 has been tossed the most times.")