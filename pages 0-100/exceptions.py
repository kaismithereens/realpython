try:
	number = int(input("Enter an integer: "))
except ValueError:
	print("That was not an integer.")
	
def divide(num1, num2):
	try:
		print(num1/num2)
	except (TypeError, ZeroDivisionError):
		print("encountered an error")
		
try:
	number1 = int(input("Enter a non-zero integer:"))
	print("10 / {} = {}".format(number1, 10.0 / number1))
except ValueError:
	print("You didn't enter an integer.")
except ZeroDivisionError:
	print("You cannot enter 0.")