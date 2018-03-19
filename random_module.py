from random import randint
#print(randint(0,1))

heads = 0
tails = 0

for trials in range(0,10):
	while randint(0,1) == 0:
		tails = tails+1
	heads = heads+1

print(heads)
print(tails)	
print ("heads / tails =", heads/tails)
