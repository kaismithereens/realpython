def convert_to_fahrenheit(temp):
	F = temp * 9/5 + 32
	return F
def convert_to_celsius(temp):
	C = (temp - 32) * 5/9
	return C

user_inputF = input("F :")
user_inputF = int(user_inputF)
user_inputC = input("C :")
user_inputC = int(user_inputC)
	
print(f"{user_inputF} degrees F = {convert_to_celsius(user_inputF)} degrees C")
print(f"{user_inputC} degrees C = {convert_to_fahrenheit(user_inputC)} degrees F")