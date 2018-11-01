import os

my_path = r"C:\Users\ante\code\python\realpython"

input_file_name = os.path.join(my_path, "hi.txt")

with open(input_file_name, "r") as my_input_file:
	for line in my_input_file.readlines():
		print(line),