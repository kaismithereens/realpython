import os

my_path = r"C:\Users\ante\code\python\book1-exercises\chp09\practice_files\images"

file_list = os.listdir(my_path)

for file_name in file_list:
	if file_name.lower().endswith(".jpg"):
		print("Converting {} to GIF...".format(file_name))
		full_file_path = os.path.join(my_path, file_name)
		new_file_path = full_file_path[:len(full_file_path)-4] + ".gif"
		os.rename(full_file_path, new_file_path)