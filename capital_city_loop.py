from capitals import capitals_dict
import random

state = random.choice(list(capitals_dict.keys()))
capital = capitals_dict[state]

def my_function(state, capital):
	while True:
		guess = input("What is the capital of {}?".format(state))
		if guess == "exit" or guess == "EXIT" or guess == "Exit":
			print("The capital of {} is {}".format(state, capital))
			print("Goodbye")
			break
		elif guess == capital or guess == capital.lower():
			print("Correct!")
			break
			
my_function(state, capital)