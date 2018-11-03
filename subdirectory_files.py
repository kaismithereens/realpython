import glob
import os

my_path = r"C:\Users\ante\code\python\book1-exercises\chp09\practice_files\images"
possible_files = os.path.join(my_path, "*/*.png")

for file_name in glob.glob(possible_files):
	print(file_name)