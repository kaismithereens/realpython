from random import randint

flips = 0
trials = 10000

for i in range(1, trials):
	if randint(0,1) == 0:
		flips += 1
		while randint(0,1)!= 1:
			flips = flips + 1
	else:
		flips += 1
		while randint(0,1)!= 0:
			flips = flips + 1

print("The average number of flips was:",flips/trials)
	