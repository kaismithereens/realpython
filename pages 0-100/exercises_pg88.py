while True:
	try:
		user_input = int(input("Enter an integer:"))
	except ValueError:
		print("Please try again. Enter an integer:")
		continue
	break
print(user_input)