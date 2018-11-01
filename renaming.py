import os

my_path = r"C:\Users\ante\code\python\book1-exercises\chp09\practice_files\images"

file_name_list = os.listdir(my_path)

for file_name in file_name_list:
	if file_name.lower().endswith(".gif"):
		print('Converting "{}" to JPG...'.format(file_name))
		full_file_name = os.path.join(my_path, file_name)
		new_file_name = full_file_name[0:len(full_file_name)-4] + ".jpg"
		os.rename(full_file_name, new_file_name)