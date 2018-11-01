with open("poem.txt", "r") as my_input:
	for line in my_input.readlines():
		print(line, end="")