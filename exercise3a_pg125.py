my_input = open("poem.txt", "r")
my_output = open("output.txt", "w")

for line in my_input.readlines():
	my_output.writelines(line)

my_input.close()
my_output.close()