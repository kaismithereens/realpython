import glob
import os

my_path = r"C:\Users\ante\code\python\book1-exercises\chp09\practice_files\images"
possible_files = os.path.join(my_path, "*.jpg")

for file_name in glob.glob(possible_files):
	print("Converting {} to GIF...".format(file_name))
	full_file_name = os.path.join(my_path, file_name)
	new_file_name = full_file_name[0:len(full_file_name)-4] + ".gif"
	os.rename(full_file_name, new_file_name)