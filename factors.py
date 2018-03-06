user_input = input("Enter a positive integer:")
user_input = (int)(user_input)

i = 1
while(i <= user_input):
	if(user_input % i == 0):
		print(f"{i} is a divisor of {user_input}")
	i = i + 1
