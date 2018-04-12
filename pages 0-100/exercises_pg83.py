
while True:
	user_input = input("Press q or Q to quit:")
	if user_input == "q":
		break
	elif user_input == "Q":
		break
	else:
		continue
print()
		
for number in range(1, 51):
	if number % 3 == 0:
		continue
	elif number % 3 == 1:
		print(number)
	elif number % 3 == 2:
		print(number)
		