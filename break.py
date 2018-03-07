for i in range (0, 4):
	if i==2:
		break
	print(i)
	
print("Finished with i= ", str(i))
print()

for j in range(0, 4):
	if j==2:
		continue
	print(j)
	
print("Finished with j= ",str(j))
print()

phrase = "it marks the spot"

for letter in phrase:
	if letter == "X":
		break
else:
	print("There was no 'X' in the phrase")
print()

tries = 0

while tries < 3:
	password = input("Password:")
	if password == "humana":
		break
	else:
		tries = tries + 1
else:
	print("Suspicious activity.")