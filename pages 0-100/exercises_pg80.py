user_input = input("Please enter a word:")
if len(user_input)< 5:
	print("The word is shorter than 5 characters")
elif len(user_input)>5:
	print("The word is longer than 5 characters")
else:
	print("The word is 5 characters long")