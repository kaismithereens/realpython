with open("poem.txt", "r") as my_input, open("output.txt", "w") as my_output:
	for line in my_input.readlines():
		my_output.writelines(line)
		