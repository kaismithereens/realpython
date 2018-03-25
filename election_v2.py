from random import random

candidate_A = 0
candidate_B = 0

def election(rate):
	for i in range(1, 10001):
		candidate_A = 0
		candidate_B = 0
		if random() < rate:
			candidate_A = candidate_A + 1
		else:
			candidate_B = candidate_B + 1
	return candidate_A, candidate_B

candidate_A_region1, candidate_B_region1 = election(0.87)
	
if candidate_A_region1 > candidate_B_region1:
	candidate_A = candidate_A + 1
	print("Candidate A won region 1")
else:
	candidate_B = candidate_B + 1
	print("Candidate B won region 1")
	
candidate_A_region2, candidate_B_region2 = election(0.65)

	
if candidate_A_region2 > candidate_B_region2:
	candidate_A = candidate_A + 1
	print("Candidate A won region 2")
else:
	candidate_B = candidate_B + 1
	print("Candidate B won region 2")
	
candidate_A_region3, candidate_B_region3 = election(0.17)
		
if candidate_A_region3 > candidate_B_region3:
	candidate_A = candidate_A + 1
	print("Candidate A won region 3")
else:
	candidate_B = candidate_B + 1
	print("Candidate B won region 3")

print()		
if candidate_A > candidate_B:
	print("Candidate A won the election")
else:
	print("Candidate B won the election")
	