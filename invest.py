def invest(amount, rate, time):
	result = amount
	print(f"principal amount: ${amount}")
	print(f"annual rate of return: {rate}")
	for i in range(1, time + 1):
		result = result + (result * rate)
		print(f"year {i}: ${result}")

invest(100, .05, 8)
print()
invest(2000, .025, 5)