with open("helo.txt", "r") as my_input, open("hi.txt", "w") as my_output:
	for line in my_input.readlines():
		my_output.write(line)