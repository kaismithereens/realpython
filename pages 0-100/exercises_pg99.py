desserts = ["ice cream", "cookies"]
desserts.sort()
print(desserts)
print(desserts.index("ice cream"))

food = []
food = desserts[:]
food.extend(["broccoli", "turnips"])
print(food)
print(desserts)

food.remove("cookies")
print(food[0:2])

breakfast = []
my_string = "cookies, cookies, cookies"
breakfast = my_string.split(",")
print(breakfast)

def funtion(my_list):
	my_result = []

	for i in range(len(my_list)):
		if my_list[i] < 21:
			my_result.append(my_list[i])
			
	return my_result
	
print(funtion([2, 4, 8, 16, 32, 64]))