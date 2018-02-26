def square(number):
	sqr_num = number ** 2
	return sqr_num

def return_difference(num1, num2):
	"""Return difference between two numbers.
	Substracts n2 from n1"""
	return num1 - num2
	
def add_two_numbers(num1, num2):
	return num1 + num2
	
input_num = 5
output_num = square(input_num)

print(output_num)
print(return_difference(3, 5))
print(add_two_numbers(3,5))
