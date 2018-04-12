from random import randint

flips = 0
trials = 10000

def count_flips(flips, number):
	while randint(0,1) != number:
		flips += 1
	return flips

for i in range(1, trials):
	if randint(0,1) == 0:
		flips += 1
		flips = count_flips(flips, 1)
	else:
		flips += 1
		flips = count_flips(flips, 0)

print("The average number of flips was:",flips/trials)
	