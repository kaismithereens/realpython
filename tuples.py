my_tuple = ("you'll", "never", "change", "me")
print(my_tuple)
print(my_tuple[2])
print(my_tuple.index("me"))

def adder_subtractor(num1, num2):
	add = num1 + num2
	subtract = num1 - num2
	return add, subtract
	
print(adder_subtractor(3, 2))

test = adder_subtractor(4, 3)
print(test)
print(type(test))

coordinates = 4.21, 9.29
print(coordinates)
x, y = coordinates
print(x)
print(y)

str1, str2, str3 = "a", "b", "c"
print(str1)
print(str2)
print(str3)