n = 1
while (n < 5):
	print("n =", n)
	n = n + 1
print("Loop finished")

for n in range(1, 5):
	print("n =", n)
print("Loop finished")

for n in range(1, 4):
	for j in ["a", "b", "c"]:
		print("n =", n, "and j =", j)
